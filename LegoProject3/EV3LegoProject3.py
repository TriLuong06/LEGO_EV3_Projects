#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random
import string

ultra_sensor = UltrasonicSensor(Port.S3)
line_sensor1= ColorSensor(Port.S2)
line_sensor2= ColorSensor(Port.S4)


left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

stop_watch = StopWatch()

ev3 = EV3Brick()

drive_speed = 100 # mm/s
correction_turn = -6 # Degrees

drive = True
has_done_check_turn = False

def do_random_entertainment():
    drive = False
    drive_base.stop()
    choice1 = lambda: ev3.speaker.beep(frequency=400, duration=150)

    choice2 = lambda: ev3.speaker.beep()

    notes = ['C4/4','D4/4','E4/4','D4/4','C4/1']
    choice3 = lambda: ev3.speaker.play_notes(notes, tempo=120)

    choice4 = lambda: ev3.speaker.say("Woah, cool")

    choices_of_entertainment = [choice1, choice2, choice3, choice4]
    chosen = random.choice(choices_of_entertainment)
    chosen()
    drive = True


while True:
    if drive: # Roboten kjører 
        drive_base.drive(drive_speed, 0)
        
    stop_watch.resume()
    if line_sensor1.color() == Color.BLACK: # Holder roboten innenfor den svarte linjen, dersom en av sensorene på venstre/høyre side ser svart vil den snu
        drive_base.turn(correction_turn)
    elif line_sensor2.color() == Color.BLACK:
        drive_base.turn(-correction_turn)
    
    
    if ultra_sensor.distance() <= 150:
        drive = False
        ev3.speaker.play_file(SoundFile.FANFARE)
    else:
        drive = True

    if stop_watch.time() >= 10000: # Gjør en random entertainment når stopwatch når 10 sekund
        do_random_entertainment()
        stop_watch.reset() # Resetter stopwatch
