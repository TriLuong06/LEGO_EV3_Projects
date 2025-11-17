#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase


class RaceRobot: # Definer klassen til programmet
    def __init__(self):
        self.ev3 = EV3Brick()
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C) # Sett opp variabler
        self.drop_motor = Motor(Port.D)
        self.stop_watch = StopWatch()
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=104)
        self.line_sensor = ColorSensor(Port.S3)

        self.BLACK = 10 # Calibrate values for line-following
        self.WHITE = 95
        self.threshold = (self.BLACK + self.WHITE) / 2

        self.DRIVE_SPEED = 140 # Setup variables for speed and turning
        self.PROPORTIONAL_GAIN = 1.95

        self.has_dropped = False # Variables for functionality
        self.start = False

    def drop_barrier(self): # Drop barrier at start
        if not self.has_dropped: # This ensures it only happens once
            self.drop_motor.run_time(50, 1000, then=Stop.HOLD, wait=False) # Drop whilst driving, no waiting
            self.has_dropped = True

    def run(self): # Run loop for code
        while True: # Runs forever
            if Button.UP in self.ev3.buttons.pressed(): # Starts robot when UP is pressed
                self.start = True

            if self.start:
                # Drop once
                self.drop_barrier() # Drop barrier first thing

                # Line following logic
                deviation = self.line_sensor.reflection() - self.threshold

                if deviation < 0: # Make the robot turn slower to the right than to the left
                    deviation /= 3

                if deviation > 5: # If the robot strays far from the line, slow down to find it again
                    if self.DRIVE_SPEED > 100:
                        self.DRIVE_SPEED /= (deviation * 0.15)
                        wait(100)
                else:
                    self.DRIVE_SPEED = 140

                turn_rate = self.PROPORTIONAL_GAIN * deviation
                self.robot.drive(self.DRIVE_SPEED, turn_rate) # Drive and turn dynamically depending on variables



robot = RaceRobot() # Instantiate this class
robot.run() # Run the code in this class
