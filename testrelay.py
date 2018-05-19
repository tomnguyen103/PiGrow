# This code is to turn The light Source and OTHER
#possible sorts of electrical  sources.  Set to go on at 6AM and OFF at 6PM
import RPi.GPIO as GPIO
import datetime
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)    #RESET
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

        GPIO.output(18, 0)
        GPIO.output(18, 1)
        sleep (0.5)
        GPIO.output(18, 0)
        GPIO.cleanup()

    if time == lxoff:
        GPIO.output(18, 0)
        GPIO.output(18, 1)
        sleep (0.5)
        GPIO.output(18, 0)
        GPIO.cleanup()

GPIO.setwarnings(False)

    #sleep(5)
