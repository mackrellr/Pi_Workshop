import RPi.GPIO as GPIO
import time

# This is added b/c a loop will be broken via Ctrl C
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

trig = 18
echo = 24
red_led = 16
yellow_led = 20
green_led = 21

# Set pins (IN/OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

def green_light():
    GPIO.output(green_led, GPIO.HIGH)
    GPIO.output(yellow_led, GPIO.LOW)
    GPIO.output(red_led, GPIO.LOW)

def yellow_light():
    GPIO.output(yellow_led, GPIO.HIGH)
    GPIO.output(red_led, GPIO.LOW)
    GPIO.output(green_led, GPIO.LOW)

def red_light():
    GPIO.output(red_led, GPIO.HIGH)
    GPIO.output(yellow_led, GPIO.LOW)
    GPIO.output(green_led, GPIO.LOW)

def get_distance():
    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.outpout(trig, False)

    while GPIO.input(echo) == False:
        start = time.time()

    while GPIO.input(echo) == True:
        end = time.time()

    sig_time = end - start

    # distance = rate / time (cm)
    distance = sig_time / 0.000058 # inches: 0.000148
    print('Distance: {} cm'.format(distance))
    return distance

while True:
    distance = get_distance()
    time.sleep(0.05)
    
    if distance >= 9: # in cm
        green_light()
    elif 9 > distance > 6:
        yellow_light()
    elif distance <=6:
        red_light()
