#!/usr/bin/python
import serial
import time
ser = serial.Serial("/dev/ttyUSB0",baudrate=9600)
while True:
    bytesToRead = ser.inWaiting()
    data = ser.read(bytesToRead)
    if(bytesToRead):
        my_hex = data.decode('hex') 
        print " ".join(hex(ord(n)) for n in my_hex) 
