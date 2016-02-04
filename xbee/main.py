import XBee
import serial
from time import sleep
from multiprocessing import Pool

def Read():
    while True:
        Msg = xbee.Receive()


if __name__ == "__main__":
    xbee = XBee.XBee("/dev/ttyUSB0")  # Your serial port name here
    # A simple string message
#    sent = xbee.SendStr("Hello World")
    while True:
        xbee.Send("00")
        xbee.Send("10")
        xbee.Send("20")
        xbee.Send("30")
    while True:
        xbee.Send("10")
        sleep(0.25)
        xbee.Send("01")
        sleep(0.25)
        xbee.Send("21")
        sleep(0.25)
        xbee.Send("31")
        sleep(0.25)
        xbee.Send("10")
        sleep(0.25)
        xbee.Send("00")
        sleep(0.25)
        xbee.Send("20")
        sleep(0.25)
        xbee.Send("30")
        sleep(0.25)
 
    Read()
    #while True:
     #   Msg = xbee.Receive()
      #  if Msg:
       #     xbee.Send("hello world")
        #    sleep(0.25)
         #   content = Msg[7:-1]
          #  print("Msg: " + xbee.format(content))


    # A message that requires escaping
    #sleep(0.25)
    #Msg = xbee.Receive()
    #if Msg:
     #   content = Msg[7:-1]
      #  print("Msg: " + xbee.format(content))
