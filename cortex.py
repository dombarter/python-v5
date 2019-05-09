# Imports

import sys
import math
import vex

# Motors

leftMotor = vex.Motor(1)
rightMotor = vex.Motor(2,True)

# Controller

controller = vex.Joystick()

# Functions

def stopMotors():
    leftMotor.off()
    rightMotor.off()

def goForwards():
    leftMotor.run(100)
    rightMotor.run(100)

def goBackwards():
    leftMotor.run(-100)
    rightMotor.run(-100)

# Main

while True:

    if(controller.axis2() > 10):
        goForwards()
    elif(controller.axis2() < -10):
        goBackwards()
    else:
        stopMotors()

