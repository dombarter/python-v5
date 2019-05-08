
import sys 
import vex
from vex import *
import math

brain = vex.Brain()
leftMotor   = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False) 
rightMotor  = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
controller  = vex.Controller(vex.ControllerType.PRIMARY)

def stopMotors():
    leftMotor.stop(vex.BrakeType.BRAKE)
    rightMotor.stop(vex.BrakeType.BRAKE)

def goForwards():
    leftMotor.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
    rightMotor.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)

def goBackwards():
    leftMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)
    rightMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)

while True:

    if controller.axis3.value() > 10:
         goForwards()
    elif controller.axis3.value() < -10:
        goBackwards()
    else:
        stopMotors()
