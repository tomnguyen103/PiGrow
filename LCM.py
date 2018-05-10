# This code is to turn The light Source and OTHER source
#light is programmed to automatically go on at 6 AM and off 6PM
import RPi.GPIO as GPIO
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)    #OPEN
GPIO.setup(16, GPIO.OUT)    #CLOSE

GPIO.output(16, 1)          #Reset Relay
sleep (0.1)
GPIO.output(16, 0)

lxon = "06:00"
lxoff = "18:00"

while True:
    time = datetime.datetime.now().strftime("%H:%M")
    if time == lxon:

        GPIO.output(16, 0)
        GPIO.output(16, 1)
        sleep (0.5)
        GPIO.output(16, 0)
        GPIO.cleanup()

    if time == lxoff:
        GPIO.output(16, 0)
        GPIO.output(16, 1)
        sleep (0.5)
        GPIO.output(16, 0)
        GPIO.cleanup()

GPIO.setwarnings(False)
