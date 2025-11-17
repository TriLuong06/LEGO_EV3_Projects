#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class TrashRobot:
    def __init__(self):

        # Initialises the motors and sensors.
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.D)
        self.shovel = Motor(Port.B)
        self.sensor = UltrasonicSensor(Port.S2)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=104)
        self.robot.settings(200, 100, 200, 100)

        self.objectPickedUp = False

    def run(self):
        # Main code:
        while True:
            # Begins the program for picking up things with the shovel
            # When sensor senses an object in the robot's path.
            if self.sensor.distance() < 400 and not self.objectPickedUp:
                self.robot.stop()
                self.shovel.run_time(-100, 1600, then=Stop.HOLD, wait=True)
                wait(100)
                self.robot.settings(700, 700, 0, 0)
                self.robot.straight(350)
                self.shovel.run_time(100, 1600, then=Stop.HOLD, wait=True)
                wait(100)
                self.robot.stop()
                self.robot.settings(400, 400, 200, 100)

                # If there still are objects in front of robot after pickup, turn away.
                if self.sensor.distance() < 200:
                    self.objectPickedUp = True

            # If obstruction is not removed, robot will drive away
            elif self.objectPickedUp:
                self.robot.straight(-300)
                self.robot.stop()
                self.robot.settings(200, 100, 200, 100)
                self.robot.turn(180)
                self.objectPickedUp = False

            # If nothing in path, drive forward
            else:
                self.robot.drive(100, 0)
