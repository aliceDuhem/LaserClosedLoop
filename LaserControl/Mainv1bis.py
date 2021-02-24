#COntrol the motor with the library search, Without PID

import pyvisa as visa
# from GetPower import PowerMeter
from guizero import App,Text,TextBox, PushButton
from ratioCodes import *
from characteristics import Characteristics
from time import sleep
import threading
#from GetPower import PowerMeter


##Don't use OOP: makes things more difficult
#INTERESTING RESOURCE: https://stackabuse.com/local-and-global-variables-in-python/

# _______________________________________________________________________________________________
# import RPi.GPIO as GPIO # THIS MODULE MUST BE INSTALLED DIRECTLY ON RASPBERRI PI


# # power on the RPi and command initialisation

#initialise power meter
#pm = PowerMeter() #puts an error in the command window if power meter not plugged in

# Ask the user for a power value (as area is constant and intensity is power*Area and we use the ratio)
#-----------------------------------------------------------------------------
#Constant values
MIN_VALUE_POWER=0
MAX_VALUE_POWER=10000
MIN_TRANSMITTANCE=0
MAX_TRANSMITTANCE=1
MIN_INCREMENT=0.000001
MAX_INCREMENT=4

#-----------------------------------------------------------------------------
#Initialise the values that are being used
motorIncrement = 0
outputValue = 0
HWPTransmittance = 0
cubeTransmittance = 0

#-----------------------------------------------------------------------------

#Initialise the object which contains the values
def validation():
    if correct_entry_type(desiredPower.value)==True:
        if correct_entry_range_power(float(desiredPower.value))==True:
            outputValue=desiredPower.value
        else:
            outputValue= "Please enter a value in the range 0-10000"
    else:
        outputValue= "Please enter a number"

    if correct_entry_type(motorInc.value)==True:
        if correct_entry_range_increment(float(motorInc.value))==True:
            motorIncrement=motorInc.value

        else:
            motorIncrement= "Please enter a value in the range 0.001-2"
    else:
        motorIncrement= "Please enter a number"

    if correct_entry_type(HWPTrans.value)==True:
        if correct_entry_range_transmittance(float(HWPTrans.value))==True:
            HWPTransmittance=HWPTrans.value
        else:
            HWPTransmittance= "Please enter a value in the range 0-1"
    else:
        HWPTransmittance= "Please enter a number"

    if correct_entry_type(CubeTrans.value)==True:
        if correct_entry_range_transmittance(float(CubeTrans.value))==True:
            cubeTransmittance=CubeTrans.value
        else:
            cubeTransmittance= "Please enter a value in the range 0-1"
    else:
        cubeTransmittance= "Please enter the range"

    print(outputValue)



#Function that checks if the values is an float
def correct_entry_type(float_output):
    try:
        outputVal = float(float_output)
        return True
    except ValueError:
        print("Please enter a number")
        return False

#Function that checks if the values is in a correct range
def correct_entry_range_power(float_output):
    if (float_output >= MIN_VALUE_POWER) and (float_output <= MAX_VALUE_POWER):
        return True
    else:
        print("Please enter a value in the range 0-10000")
        return False

def correct_entry_range_increment(float_output):
    if (float_output >= MIN_INCREMENT) and (float_output <= MAX_INCREMENT):
        return True
    else:
        print("Please enter a value in the range 0.001-2")
        return False

def correct_entry_range_transmittance(float_output):
    if (float_output >= MIN_TRANSMITTANCE) and (float_output <= MAX_TRANSMITTANCE):
        return True
    else:
        print("Please enter a value in the range 0-1")
        return False

#-----------------------------------------------------------------------------

#App Display
app= App(title="Closed Loop Laser Intensity Regulator")
welcomeMessage = Text(app,text="Welcome to the Closed Loop Laser intensity regulator software",
                      size=30,color='black')
boxPowerMessage=Text(app,text="Enter the desired laser output power")
#Textbox where the user enters the desired power
desiredPower=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxIncMessage=Text(app,text="Enter the motor Increment")
#Textbox where the user enters the desired power
motorInc=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxHWPMessage=Text(app,text="Enter the half wave plate transmittance")
#Textbox where the user enters the desired power
HWPTrans=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxCubeMessage=Text(app,text="Enter the cube transmittance")
#Textbox where the user enters the desired power
CubeTrans=TextBox(app,width=50,height=10)

blank=Text(app,text="")

#Button that validates the entry and stores the textbox value as desired output
validation=PushButton(app,command=validation,text="Validate Entry")

#Text off all the characteristics
output_val=Text(app,text="Wanted Power:")
outputVal_text.value = outputValue
outputValue_text=Text(app,text="")

increment_val=Text(app,text="Motor Increment:")
motorIncrement=Text(app,text="")
HWPTrans_val=Text(app,text="Half Wave PLate Transmittance:")
HWPTransmittance=Text(app,text="")
Cube_val=Text(app,text="Cube Transmittance:")
cubeTransmittance=Text(app,text="")




# Rotate to 0

# Put the correct angle and remember the angle_motor

# Make the dictionary (for optical components)
# TODO: sync variableNames With APP.Py for dictionary creation
#ratio_dict = ratio.find_ratioDict(laser_values.stepperIncrement, laser_values.cube_transmittance,laser_values.cube_ref_trans)

#Loop:
    # Reads the value from the power PowerMeter

    # angle at which halfwave plate needs to be at
#neededAngle = difference.neededAngle(laser_values.current_motor_angle, laser_values.Pd ,laser_values.wantedIntensity, ratio_dict)

    # Find the angle of intended rotation
    # Send the angle to RPi (with GIPO-0)
    # Deconstruct the second dictionary
    # Write values in CSV (or in data array)
#end of the loop

#Optionanl - send back to 0
#Write the values in CSV file for data analysis
#  destroy main DICTIONARY
#del ratio_dict

#Shut down the guizero when close button pressed
app.display()
# Shut RPi
