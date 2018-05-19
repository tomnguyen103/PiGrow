import paho.mqtt.client as mqtt
import time
from config import get_parameter, db_session
from models import GobbleDGookObsfucation
import datetime

import logging

logger = logging.getLogger(__name__)

BASE_NAME = 'whatever'


def on_connect(client, userdata, flags, rc):
    m = "Connected flags = " + str(flags) + " result code = " +\
        str(rc) + " client1_id  =" + str(client)
    logger.info(m)


def create_mqtt_client(name):
    """
    Uses configuration files to setup a connection to mqtt server.
    Then starts a background thread to process messages.
    Remember to loop_stop() and disconnect() when no longer needed.

    param: name : str : instance name of paho-mqtt client
    returns paho.mqtt.client.Client
    """
    tls_ca_cert = app_config.get_parameter('tls', 'ca_cert')
    mqtt_client = mqtt.Client(name)    # create new instance
    #attach functions to callback
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.on_subscribe = on_subscribe

    # setup tls encryption
    if tls_ca_cert != 'Missing' and len(tls_ca_cert.strip()) > 0:
        tls_cert_file = app_config.get_parameter('tls', 'certfile', None)
        tls_key_file = app_config.get_parameter('tls', 'keyfile', None)
        mqtt_client.tls_set(ca_certs=tls_ca_cert, certfile=tls_cert_file,
            keyfile=tls_key_file)
        logger.debug('Using encryption [ca_certs=' + tls_ca_cert +
            ', certfile=' + tls_cert_file +
            ', keyfile=' + tls_key_file)

    # Set up username and password
    # be sure to use tls if using passwords as they are sent
    # in clear text otherwise
    user_name = app_config.get_parameter('mqtt', 'user', 'Missing!')
    password = app_config.get_parameter('mqtt', 'password', 'Missing!')
    if user_name != 'Missing!'and password != 'Missing!':
        mqtt_client.username_pw_set(username=user_name, password=password)

    broker_address = app_config.get_parameter('mqtt', 'server', 'localhost')
    try:
        broker_port = app_config.get_parameter_int('mqtt', 'port', '1883')
    except ValueError:
        broker_port = 1883
        logger.debug('Failed to parse port as integer from config file')

    logger.debug(
        'Attempting to connect(server='
        + broker_address + ', port='
        + str(broker_port) + ')'
        )
    mqtt_client.connect(broker_address, port=broker_port)  # connect to broker
    mqtt_client.loop_start()  # start message processing in background

    return mqtt_client


def send_alerts():
    session = db_session()
    results = session.query(GobbleDGookObsfucation).filter_by(
        alert_sent='No'
        ).all()
    now = datetime.datetime.utcnow()
    topic = get_parameter('mqtt', 'topic')
    client1 = create_mqtt_client()
    try:

        for row in results:
            send_alert = now < row.date_expires

            logger.info("[code=" + row.code + ', '
                    + 'expires=' + str(row.date_expires) + ', '
                    + 'alert_sent=' + row.alert_sent + ', '
                    + 'send_alert=' + str(send_alert) + ']')

            if not send_alert:
                logger.info('Too late to send alert for code ' + row.code)
                row.alert_sent = 'Too late'
                row.date_alert_sent = now
                session.add(row)
                session.commit()
            else:
                logger.info('Alert sent for code ' + row.code)
                client1.publish(topic, row.to_json(), 1)
                row.alert_sent = 'Yes'
                row.date_alert_sent = now
                session.add(row)
                session.commit()

    finally:
        client1.loop_stop()
        client1.disconnect()
