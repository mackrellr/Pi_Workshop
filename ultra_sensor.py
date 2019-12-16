import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 18
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, True)
time.sleep(0.0001)
GPIO.outpout(trig, False)

while GPIO.input(echo) == False:
    start = time.time()

while GPIO.input(echo) == True:
    end = time.time()

sig_time = end - start

# cm
distance = sig_time / 0.000058 # inches: 0.000148
print('Distance: {} cm'.format(distance))

GPIO.cleanup()