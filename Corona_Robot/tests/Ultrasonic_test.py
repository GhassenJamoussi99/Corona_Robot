import sys
sys.path.append('../')
from distance_sensor import *

init()

while True:
    forward(0)
    if check() == False:
        break



stop()
