import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode (GPIO.BCM)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (aux, GPIO.IN, GPIO.PUD_UP)

for i in range (8):
    print (GPIO.input(aux[i]))

while True:
    for i in range (7):
        GPIO.output (leds[i], GPIO.input(aux[i]))
        #time.sleep (1)

GPIO.output (leds, 0)

GPIO.cleanup()
