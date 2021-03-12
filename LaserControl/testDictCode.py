#COntrol the motor with the library search, Without PID and user input

import pyvisa as visa
import os
import datetime
from GetPower import PowerMeter
from ratioCodesv2 import ratiov2 as ratio
from ratioCodesv2 import differencev2 as difference
from ratioCodesv2 import absolutev2 as absolute
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
motorIncrement = 0.2
wantedPower = [0.00001,0.00005,0.00008,0.0001,0.00015,0.00016,0.00017,0.00018,0.00019,0.0002,0.0003,0.0004,0.0005,0.00055,0.00056,0.00057,0.00058,0.00059,0.0006,0.0007,0.0008,0.00085,0.00086,0.00087,0.00088,0.00089,0.0009,0.00095,0.001,0.0015,0.002,0.005]
HWPTransmittance = 0.1
cubeTransmittance = 0.1
cubeRefTransmittance=0.5
current_motor_angle=45
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
    del oriDictionary[0]

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
    fileName = docName+'_motorInc'+str(motorIncrement)+'_'+date_time+file_extension
    columns = ['wanted Power experiment','power at power_meter','angle'] #determines the 3 columns of the file
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

data_array=[]
pm = PowerMeter()
#motor_to_0(pm)
max_power=pm.readPower(pm.power_meter)
#current_motor_angle=motor_to_initial_power(pm,pv,motorIncrement)


for pv in wantedPower:

    for i in range(1):
        inst_power=pm.readPower(pm.power_meter)
        ratio_dict = ratio.find_ratioDict(motorIncrement,cubeTransmittance,cubeRefTransmittance)
        #print(ratio_dict)
        """for r,angle in ratio_dict.items():
            if angle==0.0:
                del ratio_dict[r]
                break # Python cannot divide by 0"""
        del ratio_dict[0]
        #print(ratio_dict)
        #error= inst_power-pv
        anglecomputed = difference.neededAngle(current_motor_angle, inst_power,pv,ratio_dict)
        angle_rotation = current_motor_angle-anglecomputed
        a=[pv,inst_power,anglecomputed]
        data_array.append(a)
    del ratio_dict

createCsvFileData(data_array)
del data_array
