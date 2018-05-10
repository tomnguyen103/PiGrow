#your Raspberry Pi is connected to the internet.
#This is needed to track time.
#
import RPi.GPIO as GPIO
import datetime
import time

pin = OutPutPin
GPIO.setup(pin, GPIO.OUT)

while True:
    time = datetime.datetime.now().strftime("%H:%M")
    if time == "05:00":
        GPIO.output(pin, True)
        time.sleep(number_of_seconds_for_led_to_be_on_here)
        GPIO.output(pin, False)
    time.sleep(0.030)
