# Use GPIO pins 18 and 23 to make two LEDs blink

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
red_pin1 = 18
red_pin2 = 23

# Set GPIO pins to output mode
GPIO.setup(red_pin1, GPIO.OUT)
GPIO.setup(red_pin2, GPIO.OUT)
        
try:
    while True:
        GPIO.output(red_pin1, True)     # True means that LED turns on
        GPIO.output(red_pin2, False)    # False means that LED turns off
        time.sleep(0.5)                 # delay 0.5 seconds
        GPIO.output(red_pin1, False)
        GPIO.output(red_pin2, True)
        time.sleep(0.5)
finally:  
    print("Cleaning up")
    GPIO.cleanup()

