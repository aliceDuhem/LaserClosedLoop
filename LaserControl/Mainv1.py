#COntrol the motor with the library search, Without PID

import visa
# from GetPower import PowerMeter
from guizero import App,Text,TextBox, PushButton
from ratioCodes import * 
from general_characteristics import characteristics
from time import sleep


# _______________________________________________________________________________________________
# import RPi.GPIO as GPIO # THIS MODULE MUST BE INSTALLED DIRECTLY ON RASPBERRI PI


# # power on the RPi
# # initialise motor pins
# DIR = 20 # directional GPIO pin
# STEP = 21 # Step GPIO pin
# CW =1 # clockwise rotation
# CCW =0 # Anticlockwise rotation
# SPR = 200 # Steps per revolution 

# # Setup GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(STEP, GPIO.OUT)
# GPIO.output(DIR, CW)

# MODE = (14,15,16) # MS1, MS2 MS3 pin number for microstepping
# GPIO.setup(MODE, GPIO.OUT)

# # MS1, MS2, MS3 dictionary for micro-stepping size
# RESOLUTION = {'Full': (0, 0, 0),
#               'Half': (1, 0, 0),
#               '1/4': (0, 1, 0),
#               '1/8': (1, 1, 0),
#               '1/16': (0, 0, 1),
#               '1/32': (1, 0, 1)}

# # change resolution for different microstep size 
# GPIO.output(MODE, RESOLUTION['1/16'])            
# ______________________________________________________________________________________________________

#initialise power meter

# Ask the user for a power value (as area is constant and intensity is power*Area and we use the ratio)

# Rotate to 0

# Put the correct angle and remember the angle_motor

# Make the dictionary (for optical components)
# TODO: sync variableNames With APP.Py for dictionary creation
ratio_dict = ratio.find_ratioDict(characteristics.stepperIncrement, characteristics.cube_transmittance, characteristics.cube_ref_trans)

#Loop:
    # Reads the value from the power PowerMeter

    # angle at which halfwave plate needs to be at
neededAngle = difference.neededAngle(characteristics.current_motor_angle, characteristics.Pd ,characteristics.wantedIntensity, ratio_dict)

    # Find the angle of intended rotation
    # Send the angle to RPi (with GIPO-0)
    # Deconstruct the second dictionary
    # Write values in CSV (or in data array)
#end of the loop

#Optionanl - send back to 0
#Write the values in CSV file for data analysis
#  destroy main DICTIONARY
del ratio_dict
# Shut RPi
