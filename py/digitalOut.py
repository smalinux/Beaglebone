# digital out === digital write
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

# setup PINs
outPin = "P9_12"
GPIO.setup(outPin, GPIO.OUT)

for i in range(0, 5):
    GPIO.output(outPin, GPIO.HIGH) # output == write
    sleep(3)
    GPIO.output(outPin, GPIO.LOW)
    sleep(3)

# clean & release
GPIO.cleanup() # release GPIOs
