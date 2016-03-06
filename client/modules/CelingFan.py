# -*- coding: utf-8-*-
import datetime
import time
import re
from client.app_utils import getTimezone
from semantic.dates import DateService
import serial
import time
import sys
sys.path.insert(0, '../../xbee')
import XBee 

xbee = XBee.XBee("/dev/ttyAMA0") 

WORDS = ["COLD", "HOT", "FAN", "ON", "OFF", "ITS", "LITTLE"]
status=0

def handle(text, mic, profile):
    """
        Reports the current date based on the user's location.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    if bool(re.search(r'\bon\b', text, re.IGNORECASE)) or  bool(re.search(r'\bhot\b', text, re.IGNORECASE)) :
      xbee.Send("21")
    else:
      xbee.Send("20")
    message = "Yes, Sir" 
    mic.say(message)

def isValid(text):
    """
        Returns True if input is related to the date.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bon\b', text, re.IGNORECASE)) or bool(re.search(r'\bcold\b', text, re.IGNORECASE)) or bool(re.search(r'\bhot\b', text, re.IGNORECASE)) or bool(re.search(r'\off\b', text, re.IGNORECASE))
