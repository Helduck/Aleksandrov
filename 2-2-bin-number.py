import RPi.GPIO as GPIO
import time
from random import randint

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range (8):
    number[i] = randint (0, 1)

print (number)

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.output (dac, number)
time.sleep (10)
GPIO.output (dac, 0)
time.sleep (5)

for i in range (7):
    number[i] = 0

number[6] = 1

GPIO.output (dac, number)
time.sleep (10)
GPIO.output (dac, 0)

GPIO.cleanup()



