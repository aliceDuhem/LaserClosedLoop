import pyvisa as visa
import os
import datetime
from GetPower import PowerMeter
from ratioCodes import ratio
from ratioCodes import difference
from ratioCodes import absolute
from characteristics import Characteristics
from time import sleep

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
motorIncrement = 0.9
wantedPower = 0.005
HWPTransmittance = 0.98
cubeTransmittance = 0.955
cubeRefTransmittance=1
current_motor_angle=45
#-----------------------------------------------------------------------------
def createCsvFileData(data):


    docName = 'Test_Dictionary_motorInc_09_wantedPower_5_' #beginning name document
    date_time = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S")   #adds the time to the title to make it unique
    file_extension =  '.csv'    #needs the file extension in the name
    alreadyExists_str = 'second_'
    fileName = docName+date_time+file_extension
    columns = ['timestamp','power','neededAngle'] #determines the 3 columns of the file
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
    line = 'Intensity recordings for experiment starting at '+ str(data[0][0]) +'. readings every '+ str(data[1][0]-data[0][0]) + ' seconds, wanted power = 5mW \n'
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

pm = PowerMeter()

ratio_dict = ratio.find_ratioDict(motorIncrement,cubeTransmittance,cubeRefTransmittance)
# remove 0 from dict so it can work in difference.neededangle as del does not work inside
del Dict[0] # Python cannot divide by 0

data_array=[]

for i in range(5):
    inst_power=pm.readPower(pm.power_meter)
    error= inst_power-wantedPower
    neededAngle = difference.neededAngle(current_motor_angle, inst_power,wantedPower, ratio_dict)
    angle_rotation = current_motor_angle-neededAngle
    a=[datetime.datetime.now(),inst_power,neededAngle]
    data_array.append(a)
    sleep(1)


createCsvFileData(data_array)
del data_array

#  destroy main DICTIONARY
del ratio_dict
