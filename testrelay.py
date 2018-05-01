##import RPi.GPIO as GPIO
##from time import sleep
##
### The script as below using BCM GPIO 00..nn numbers
##GPIO.setmode(GPIO.BCM)
##
### Set relay pins as output
##GPIO.setup(16, GPIO.OUT)
##
###run when the power on
##def countdown(n):
##    while n > 0:
##        n = n -1
##    if n == 0:
##        GPIO.output(16, GPIO.HIGH)
##        sleep(5)
##        countdown(10)
##        GPIO.output(16, GPIO.LOW)

    
    
    
# -*- coding:utf-8 -*-
# Mini relay Featherwing
##import RPi.GPIO as GPIO
##import datetime
##from time import sleep
##
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(16, GPIO.OUT)    #RESET
##GPIO.setup(16, GPIO.OUT)    #OPEN
##GPIO.setup(16, GPIO.OUT)    #CLOSE
##
##GPIO.output(16, 1)          #Reset Relay
##sleep (5)
##GPIO.output(16, 0)
##
##lxon = "20:25"
##lxoff = "20:26"
##
##while True:
##    time = datetime.datetime.now().strftime("%H:%M")
##    if time == lxon:
##        
##
##        sleep (1)
##
##        GPIO.output(16, 0)
##        GPIO.output(27, 1)
##        sleep (0.1)
##        GPIO.output(27, 0)
##
##    if time == lxoff:
##        GPIO.output(27, 0)
##        GPIO.output(22, 1)
##        sleep (0.1)
##        GPIO.output(22, 0)
##        GPIO.cleanup()        
##        
# -*- coding:utf-8 -*-
# Mini relay Featherwing
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

lxon = "12:35"
lxoff = "12:36"

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
#while (True):
    
    # Turn all relays ON
    #GPIO.output(16, GPIO.HIGH)
    
    # Sleep for 5 seconds
    #sleep(5) 
    # Turn all relays OFF
    #GPIO.output(16, GPIO.LOW)

    # Sleep for 5 seconds
    #sleep(5)