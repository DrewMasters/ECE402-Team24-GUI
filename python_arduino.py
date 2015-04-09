__author__ = 'Drew Masters'

import serial
import time

arduino=serial.Serial(port=15, baudrate=115200, timeout=.1)
time.sleep(1)

while True:
    data=arduino.readline()[:-2]
    if data:
        print data