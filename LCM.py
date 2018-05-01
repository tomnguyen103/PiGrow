#! /usr/bin/python
# Import the libraries we need
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
# Set the LED GPIO number
LCM = 16
# Set the LED GPIO pin as an output
GPIO.setup(LCM, GPIO.OUT)
# Turn the GPIO pin on
GPIO.output(LCM,True)
# Wait 5 seconds
time.sleep(5)
# Turn the GPIO pin off
GPIO.output(LCM,False)
#wait 10 second
time.sleep(10)
#turn back on the light if necessesary
GPIO.output(LCM,True)
time.sleep(5)
#shut down the light
GPIO.output(LCM,False)
