#!/usr/bin/python3
from inputd import *

process
if process=="add":
    addition()
elif process=="sub":
    subraction()
elif process=="mult":
    multiplication()
elif process=="div":
    division()
elif process=="perc":
    Percentage()
else:
    print("Invalid Process...")