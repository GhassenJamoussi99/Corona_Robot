from motorControl import init
from distance_sensor import check
import RPi.GPIO as GPIO
import pygame

def follow():
    OK=0
    init()
    GPIO.setup(21,GPIO.IN) #Right
    GPIO.setup(20,GPIO.IN) #Left
    pygame.init()
    screen = pygame.display.set_mode([240, 160])

    try:
        while True:
            if check():
                if GPIO.input(20):
                    GPIO.output(4,True)
                else:
                    GPIO.output(4,False)
                
                if GPIO.input(21):
                    GPIO.output(27,True)
                else:
                    GPIO.output(27,False)
                
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        stop()
                        OK = 1
                        pygame.quit()
            
            if OK == 1:
                break
                
            
    finally:
        GPIO.cleanup()
