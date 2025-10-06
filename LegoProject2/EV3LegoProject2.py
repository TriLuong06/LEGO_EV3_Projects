#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

ultra_sensor = UltrasonicSensor(Port.S1)
button1 = TouchSensor(Port.S2)

program_start = False # Styrer om programmet er ferdig eller ikke

while True:
    if button1.pressed(): # Når knappen på siden trykkes, starter/stoppes programmet. program_start flippes fra False til True
        drive_base.stop()
        if program_start == False:
            ev3.speaker.say("Exercise 2")
        else:
            ev3.speaker.say("Exercise done")
        program_start = not program_start # Her settes verdien av program_start til det motsatte av seg selv


    if program_start:
        if ultra_sensor.distance() >= 200: # Hvis det ikke er en hindring rett foran, kan den kjøre frem fritt
            drive_base.drive(100, 0)  # Kjør rett frem
        else:
            drive_base.stop()
            drive_base.turn(90) # Snu 90 grader
            wait(50)