import pygame
from motorControl import *
from distance_sensor import check
GPIO.setwarnings(False)

def Keyboard():
    GPIO.cleanup()
    init()
    pygame.init()
    screen = pygame.display.set_mode([240, 160])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("right")
                    turn_right()
                elif event.key == pygame.K_LEFT:
                    print("left")
                    turn_left()
                elif event.key == pygame.K_UP:
                    print("up")
                    if check():
                        forward()
                elif event.key == pygame.K_DOWN:
                    print("down")
                    reverse()
                elif event.key == pygame.K_x:
                    print("stop")
                    stop()
                elif event.key == pygame.K_q:
                    stop()
                    pygame.quit()
            elif event.type ==  pygame.KEYUP:
                print('No key pressed')
                stop()


