
import sys # import all of these!
import vex
from vex import *
import math

# you can make your own functions and classes used in the below three functions here.

def pre_auton(): # place pre-auto code here
    pass

def autonomous(): # place autonomous code here
    pass

def drivercontrol(): # palce main control code here
    while True:
        pass


competition = vex.Competition() # competition object

competition.autonomous(autonomous) # set up callbacks for the three periods
competition.drivercontrol(drivercontrol)
pre_auton()

