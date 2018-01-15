#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

BLINK_FREQ = 1

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)

def loop():
    GPIO.output(GREEN_LED, True)
    time.sleep(BLINK_FREQ)
    GPIO.output(GREEN_LED, False)
    time.sleep(BLINK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()
