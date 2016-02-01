#!/usr/bin/python
import serial
import time
ser = serial.Serial("/dev/ttyUSB0",baudrate=9600)
idx = 0 
word = "7E 00 7D 33 10 01 00 00 00 00 00 00 FF FF FF FE 00 00 68 65 6C 6C 6F DF"
word = "7E 00 7D 33 10 01 00 00 00 00 00 00 FF FF FF FE 00 00 68 65 6C 6C 6F DF" 
while True:
  ser.write(str(word))
  print word
  time.sleep(10)
  ser.write(str(word))

