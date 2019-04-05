import RPi.GPIO as GPIO

from time import sleep

failed_led = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(failed_led, GPIO.OUT, initial=GPIO.LOW)

def blink(pin_led):
    for i in range(10):
        GPIO.output(pin_led, (i % 2) == 0)
        sleep(1)

blink(failed_led)
