#From 0 to the required intensity
import os
from time import sleep
#functions needed to know the output
from ratioCodes import ratio
from ratioCodes import absolute
from ratioCodes import difference

#reads the power from power PowerMeter
from GetPower import powerMeter

#METHOD_1: directly go to the required angle and remember it
def go_to_initial_intensity():
# Set up the power meter and Dictionnary
    #---------------------------------------------------------------------------
    #the time the signal takes to go from the code to the RPi
    reaction_time_Rpi = 10
    # current motor angle, after calibration
    current_motor_angle = 0

    #Pd = powerMeter.readPower();
    Pd=1;
    
    #TODO: replace the wanted intensity by user input
    wantedIntensity = 20;
    stepperIncrement=0.45;

    # Calculates dictionary based of stepper motor increments, transmittance etc.
    oriDictionary = ratio.find_ratioDict(stepperIncrement)

    #Angle at which the motor needs to be at to achieve the wanted intensity
    additional_angle = difference.neededAngle(current_motor_angle,Pd, wantedIntensity, oriDictionary)
    #---------------------------------------------------------------------------

    #The new angle is the previous one + the angle by which the motor turns
    current_motor_angle=current_motor_angle+additional_angle;
    #TODO: enter the function that sends the code to the Rpi

go_to_initial_intensity()
