#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


#Initialising robot.
ev3 = EV3Brick()

#Initialising the two motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#Initialising the driving base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

 #ev3.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)


#Andreas' programming.
ev3.screen.draw_text(20,20,"Hello world!", text_color=Color.GREEN, background_color=Color.WHITE)
wait(200)

#Repeats the process/movements 4 times.
for n in range(4):

    #Robot moves straight forward.
    robot.straight(300)
    ev3.speaker.beep()

    #Robot turns clockwise 90 degrees.
    robot.turn(278)
    ev3.speaker.beep()


#Tri's programming
ev3.speaker.say("Have a nice day.")

    #notes=['C4/4','D4/4','E4/4','D4/4','E4/4','D4/4','C4/4']


#One beep to signalise the end of the program.
ev3.speaker.beep()

