
import sys # import all of these!
import vex
from vex import *
import math

# left motor, is plugged into port 1, has the standard gear ratio and has normal polarity
leftMotor   = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False) 

# right motor, is plugged into port 2, has the standard gear ratio and has reverse polarity
rightMotor  = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)

# will stop all the motors
def stopMotors():
    leftMotor.stop(vex.BrakeType.BRAKE)
    rightMotor.stop(vex.BrakeType.BRAKE)

    """ 
        This will make the motors brake, coming to a quick stop. You can also use:

        vex.BrakeType.HOLD - makes the motor act like a servo, menaing it cannot be turned
        vex.BrakeType.COAST - stops all current to the motor meaning it is free to move (coast)
    """

def goForwards():
    leftMotor.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)
    rightMotor.spin(vex.DirectionType.FWD,100,vex.VelocityUnits.PCT)

    """
        This will turn both of the motors forward at 100% power. 

        You can also make the motors go in reverse with:
        vex.DirectionType.REV

        100 is the percentage power and vex.VelocityUnits.PCT says 100 is a percentage. 
        You can also define the power with:
        vex.VelocityType.RPM - revolutions per minute - can go up to 200
    """

def goBackwards():
    leftMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)
    rightMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)


while True:


