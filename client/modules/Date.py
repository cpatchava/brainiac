# -*- coding: utf-8-*-
import datetime
import time
import re
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["DATE"]


def handle(text, mic, profile):
    """
        Reports the current date based on the user's location.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    service = DateService()
    response = service.convertTime(now)
    day = (time.strftime("%A")) 
    month = (time.strftime("%B"))   
    num_day = (time.strftime("%d"))  
    message = "It is " + day + "the " + num_day + "today, get over karishma" 
    mic.say(message)


def isValid(text):
    """
        Returns True if input is related to the date.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bdate\b', text, re.IGNORECASE))
