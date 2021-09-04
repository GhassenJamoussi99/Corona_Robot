import RPi.GPIO as GPIO
from motorControl import init
import time


def distance_Ultrasonic():
    GPIO.setmode(GPIO.BCM)

    TRIG = 18
    ECHO = 24


    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG,0)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(0.1)

    print("Starting Measurement...")

    GPIO.output(TRIG, 1)
    time.sleep(0.0001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    distance_cm = (stop - start) * 17000 
    GPIO.cleanup()

    return distance_cm


def check():
    init()
    if distance_Ultrasonic() < 1:
         stop()
         return False
    return True
