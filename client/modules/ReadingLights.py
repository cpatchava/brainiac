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

WORDS = ["READING", "ON", "OFF"]
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
    if bool(re.search(r'\bon\b', text, re.IGNORECASE)) :
      xbee.Send("31")
    else:
      xbee.Send("30")
    message = "Yes, Sir" 
    mic.say(message)

def isValid(text):
    """
        Returns True if input is related to the date.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\breading light\b', text, re.IGNORECASE)) 
