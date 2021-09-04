import time
import busio
import board
import adafruit_amg88xx
import signal
import os
from motorControl import stop,init
from audio.audioPlay import play


SIG = 0


def receive(signum, stack):
    global SIG
    SIG = 1


signal.signal(signal.SIGUSR1, receive)

def temp_audio():
    global SIG
    pid = os.getpid()
    with open("/tmp/prog1.pid", "w") as pidfile:
        pidfile.write(f"{pid}\n")
    i2c = busio.I2C(board.SCL, board.SDA)
    amg = adafruit_amg88xx.AMG88XX(i2c)
    init()
    while True:
        OK = 0
        print("{", end = '')
        for row in amg.pixels:
            for temp in row :
                if temp > 39 and SIG == 1:
                    stop()
                    print("Face detected and temperature above 39")
                    print("Playing audio...")
                    SIG = 0
                    play()
                    time.sleep(5)
                    OK = 1
                    break
                else:
                    print(temp,',', end = '')
                    continue
            if OK == 1:
                break
            print("")
        print("}")  
        print("\n")
        time.sleep(1)
