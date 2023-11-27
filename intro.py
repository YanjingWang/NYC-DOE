# import my_module as mm  # same directory can import directly
# from my_module import find_index, test
# from my_module import *  # hard to track down issues
# import sys  # standard library
courses = ['history', 'math', 'physics', 'CS']
# index = mm.find_index(courses,'math')
# index = find_index(courses,'math')
# print(index)
# print(test)  # print out test variable from module
# print(sys.path)  # directory-->Python path variable-->standard library-->site packages directory for 3rd party pkgs
"""what about cross directory?"""
# print("F1: hard code sys.path.append()")
# import sys
# sys.path.append('C:\Users\Ywang36\Desktop\my_module')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

print("F2: change environment variables")
"""
mac:
nano ~/.bash_profile
export PYTHONPATH=" "
CTRL+X
RESTART TERMINAL
>>>import my_module
"""

"""
windows:
advanced system settings-->environment variable PATH
add more env variables: PYTHONPATH LOCATION:
cmd: python and import my_module
"""

"""
editor+Python path
"""

"""
standard library can be used without installing 
"""

import random
random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(rads)

import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2022))

import os
print(os.getcwd())
print(os.__file__)  # location on file system

import antigravity



