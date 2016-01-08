# -*- coding: utf-8-*-
import datetime
import time
import re
from client.app_utils import getTimezone
from semantic.dates import DateService
import serial
import time
ser = serial.Serial("/dev/ttyAMA0",baudrate=9600)

WORDS = ["TURN", "ON", "LIGHTS"]

def handle(text, mic, profile):
    """
        Reports the current date based on the user's location.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    word = "H"
    ser.write(str(word))
    message = "Yes, Sir" 
    mic.say(message)

def isValid(text):
    """
        Returns True if input is related to the date.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bturn on lights\b', text, re.IGNORECASE))
