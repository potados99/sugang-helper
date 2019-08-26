# util.py
#
# This file contains some useful utility functions.

import sys
import datetime

def printnow(message, end='\n'):
	print(message, end=end)
	sys.stdout.flush()

def print_time():
    now = datetime.datetime.now()
    printnow('\n' + now.strftime("%Y-%m-%d %H:%M:%S"))
