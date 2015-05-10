# Tweet.py
# Defines Tweet class

import time

class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()
    
    
    def get_author(self):
        return self.__author
    
    
    def get_text(self):
        return self.__text
    
    
    def get_age(self):
        # What is the current time?
        now = time.time()
        
        # How many seconds, minutes, and hours have passed since tweet?
        seconds = now - self.__age
        minutes = seconds // 60
        hours = seconds // 3600
        
        # Return most significant bit
        if (hours > 0):
            return str(int(hours)) + "h"
        elif (minutes > 0):
            return str(int(minutes)) + "m"
        else:
            return str(int(seconds)) + "s"
