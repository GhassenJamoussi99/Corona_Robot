from motorControl import *
import curses

#Initialisierung von GPIO PINS
init()


screen= curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            forward()
        elif char == curses.KEY_DOWN:
            reverse()
        elif char == curses.KEY_RIGHT:
            turn_right()
        elif char == curses.KEY_LEFT:
            turn_left()
        elif char == curses.KEY_BACKSPACE:
            stop()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    stop()


GPIO.cleanup()
