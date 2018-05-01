import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
# Set the LED GPIO number
FAN = 18
# Set the LED GPIO pin as an output
GPIO.setup(FAN, GPIO.OUT)
# Turn the GPIO pin on
GPIO.output(FAN,True)
# Wait 5 seconds
time.sleep(5)
# Turn the GPIO pin off