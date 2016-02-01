import XBee
import serial
from time import sleep
from multiprocessing import Pool

def Read():
    while True:
        Msg = xbee.Recieve()


if __name__ == "__main__":
    xbee = XBee.XBee("/dev/ttyUSB0")  # Your serial port name here
    # A simple string message
#    sent = xbee.SendStr("Hello World")
#    sleep(0.25)
    xbee.Send("h")
    while True:
        Msg = xbee.Receive()
        if Msg:
            xbee.Send("hello world")
            content = Msg[7:-1]
            print("Msg: " + xbee.format(content))


    # A message that requires escaping
    sleep(0.25)
    Msg = xbee.Receive()
    if Msg:
        content = Msg[7:-1]
        print("Msg: " + xbee.format(content))
