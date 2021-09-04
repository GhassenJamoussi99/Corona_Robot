import subprocess
import pygame
import os

def play():
    os.chdir("/home/pi/Desktop/Corona_Robot/audio")
    subprocess.call('omxplayer stop.wav', shell=True)
    time.sleep(1)
    subprocess.call('omxplayer ausweis.wav', shell=True)
    time.sleep(3)
    subprocess.call('omxplayer temp_hoch.wav', shell=True)
    os.chdir("/home/pi/Desktop/Corona_Robot")
    
    
