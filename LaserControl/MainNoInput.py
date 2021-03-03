#COntrol the motor with the library search, Without PID and user input

import pyvisa as visa
import os
import datetime
from GetPower import PowerMeter
from ratioCodes import ratio
from ratioCodes import difference
from ratioCodes import absolute
from characteristics import Characteristics
from time import sleep
import threading

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
motorIncrement = 0.1
wantedPower = 0.0085
HWPTransmittance = 0.1
cubeTransmittance = 0.1
cubeRefTransmittance=0.5
current_motor_angle=0
#-----------------------------------------------------------------------------

#Definition of the functions
#-----------------------------------------------------------------------------
def motor_to_0(pm):
    pd_max_value=0
    reaction_time_Rpi = 10

    while (pm.readPower(pm.power_meter)>pd_max_value):
        #The power does not change when we read it as the plate has rotated already
        pd_max_value=pm.readPower(pm.power_meter)
        #TODO: give to the raspberry Pi an angle to rotate from, take from function
        #Wait until the RPi has changed the angle of the half wave plate
        sleep(reaction_time_Rpi)
        #test
    else:
        #TODO: tell the raspberry Pi to go one step back (which should be max power meter value)
        print("The initialisation is finished")

def motor_to_initial_power(pm,wantedPower,motorIncrement):
    # Set up the power meter and Dictionnary
    #---------------------------------------------------------------------------
    #the time the signal takes to go from the code to the RPi
    reaction_time_Rpi = 10
    # current motor angle, after calibration
    current_motor_angle = 0

    Pd = pm.readPower(pm.power_meter)
    #Pd=1;

    # Calculates dictionary based of stepper motor increments, transmittance etc.
    oriDictionary = ratio.find_ratioDict(motorIncrement)

    #Angle at which the motor needs to be at to achieve the wanted intensity
    additional_angle = difference.neededAngle(current_motor_angle,Pd, wantedPower, oriDictionary)

    #The new angle is the previous one + the angle by which the motor turns
    current_motor_angle=current_motor_angle+additional_angle;
    return current_motor_angle
    #TODO: enter the function that sends the code to the Rpi

#Create a class to write in the csv file all the data
#The columns will give the intensity and the error
def createCsvFileData(data):


    docName = 'power_readings_' #beginning name document
    date_time = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S")   #adds the time to the title to make it unique
    file_extension =  '.csv'    #needs the file extension in the name
    alreadyExists_str = 'second_'
    fileName = docName+date_time+file_extension
    columns = ['timestamp','power','error'] #determines the 3 columns of the file
    separator = ',' #separator between the 3 columns in a row
    format_columns = ['%s','%.6f','%.6f']   #the datatype of the columns

    #makes sure that the headings and the columns are of the same dimensions
    if len(data[0]) != len(columns):
        print ("The dimensions of the columns and headings are not equal")
        return

    #check if the file exists if needed in order not to overwrite
    if(os.path.exists(fileName)):
        print("The file already exists")
        fileName=docName+alreadyExists_str+date_time+file_extension

    #Specifies the path mode as writing 'w'
    file = open(fileName, 'w')

    #Writes an header/description of the document: time the measures started
    line = 'Intensity recordings for experiment starting at '+ str(data[0][0]) +'. readings every '+ str(data[1][0]-data[0][0]) + ' seconds\n'
    file.write(line)

    #each case of columns is separates on a line by a comma (separator),
    #concatenated and added to the file
    #line is a template for the format
    line = separator.join(columns)
    file.write('%s\n' % line)

    #for each new row in the data, give the correct type format
    format = separator.join(format_columns)
    for row in data:
        line= format % tuple(row)
        file.write('%s\n' % line)

    #close the file
    file.close()

def formatDateTime(date_time):
    date_time = date_time.strftime("%Y-%b-%d %H:%M:%S") #gives the correct format to the time
#-----------------------------------------------------------------------------

# # power on the RPi and command initialisation

#initialise power meter
pm = PowerMeter() #puts an error in the command window if power meter not plugged in

# Rotate to 0
motor_to_0(pm)

# Put the correct angle and remember the angle_motor
current_motor_angle=motor_to_initial_power(pm,wantedPower,motorIncrement)

# Make the dictionary (for optical components)
# TODO: sync variableNames With APP.Py for dictionary creation
ratio_dict = ratio.find_ratioDict(motorIncrement,cubeTransmittance,cubeRefTransmittance)

# remove 0 from dict so it can work in difference.neededangle as del does not work inside
del Dict[0] # Python cannot divide by 0

#Loop:
    # Reads the value from the power PowerMeter

    # angle at which halfwave plate needs to be at
#neededAngle = difference.neededAngle(laser_values.current_motor_angle, laser_values.Pd ,laser_values.wantedIntensity, ratio_dict)

    # Find the angle of intended rotation
    # Send the angle to RPi (with GIPO-0)
    # Deconstruct the second dictionary --> already done in function
    # Write values in CSV (or in data array)
#end of the loop
data_array=[]

for i in range(10):
    inst_power=pm.readPower(pm.power_meter)
    error= inst_power-wantedPower
    neededAngle = difference.neededAngle(current_motor_angle, inst_power,wantedPower, ratio_dict)
    angle_rotation = current_motor_angle-neededAngle
    a=[datetime.datetime.now(),inst_power,neededAngle]
    data_array.append(a)

#Optionanl - send back to 0
motor_to_0(pm)

#Write the values in CSV file for data analysis
createCsvFileData(data_array)
del data_array

#  destroy main DICTIONARY
del ratio_dict

#Shut down the guizero when close button pressed
# Shut RPi
