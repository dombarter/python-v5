
import sys 
import vex
from vex import *
import math

"""
    Imports all the libraries we need in order to run the robot
"""

# =========================================================

brain = vex.Brain()

"""
    Creates a new brain object, not 100% neccesary but very useful
"""

# =========================================================

leftMotor   = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False) 

rightMotor  = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)

"""
    Creates two new motors, a left and right motor.

    The left motor is plugged into port 1, has the standard gear ratio and has normal polarity

    The right motor is plugged into port 2, has the standard gear ratio and has reverse polarity
"""

# =========================================================

controller  = vex.Controller(vex.ControllerType.PRIMARY)

"""
    The controller object is used to communicate button presses and the joystick 
    positions to the brain so it can respond accordingly
"""

# =========================================================

def stopMotors():
    leftMotor.stop(vex.BrakeType.BRAKE)
    rightMotor.stop(vex.BrakeType.BRAKE)

    """ 
        This will make the motors brake, coming to a quick stop. You can also use:

        vex.BrakeType.HOLD - makes the motor act like a servo, menaing it cannot be turned
        vex.BrakeType.COAST - stops all current to the motor meaning it is free to move (coast)
    """

# =========================================================

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
# =========================================================

def goBackwards():
    leftMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)
    rightMotor.spin(vex.DirectionType.REV,100,vex.VelocityUnits.PCT)

    """
        The only difference you will notice is both of the wheels are now in reverse
    """

# =========================================================

"""
    The whole true loop is where you put all of your controls and main code.
    It is in a while loop so the code doesn't finsih straight away and can 
    constantly wait for input
"""

while True:

    if controller.axis3.value() > 10:
         goForwards()
    elif controller.axis3.value() < -10:
        goBackwards()
    else:
        stopMotors()

    """
        This is some very basic code that checks the y-axis readings of the left joystick

        If the joystick is up, the robot will move forwards,

        and if it is down the robot will reverse.

        We have added the else, to make sure the motors stop when we aren't using the joystick or
        the joystick has been moved back to a central position
    """


