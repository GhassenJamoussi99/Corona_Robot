import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)


def forward():
    GPIO.output(4,True)
    GPIO.output(17,False)
    GPIO.output(27,True)
    GPIO.output(22,False)
    time.sleep(zeit)

def reverse():
    GPIO.output(4,False)
    GPIO.output(17,True)
    GPIO.output(27,False)
    GPIO.output(22,True)

def turn_left():
    GPIO.output(4,False)  
    GPIO.output(17,True)  
    GPIO.output(27,True)  
    GPIO.output(22,False) 

def turn_right():
    GPIO.output(4,True)   
    GPIO.output(17,False)
    GPIO.output(27,False)
    GPIO.output(22,True)  

def stop():
    GPIO.output(4,False)
    GPIO.output(17,False)
    GPIO.output(27,False)
    GPIO.output(22,False)
