import pandas
import os
from random import seed
from random import random

#Generates intensity data to test the code (assume W/cm^2)
#Asks for the type of data generation - the increment it is at (first or last data)#
# And if it is case 2, gets the file name to open it
def dataGeneration(argument,laser_intensity,increment,fileArray):

    #This case gives back a random data depending on the previous one
    if (argument==1):
        seed(1)
        laser_intensity = laser_intensity+ laser_intensity*0.01*random()
        return laser_intensity

    #This case reads from a file
    elif (argument==2):
        """Method 1 using the file reading, reads the file everytime we call the function
        intensities = openRead(fileName)
        print(intensities[increment])"""

        #Method 2, read the array where the data in the file was enetered
        return fileArray[increment]

    #This case will be implemented, it takes the data from the powermeter
    elif(argument==3):
         laser_intensity= readPower()

    else:
        print("Please enter a correct argument")

#overload the previous funciton
"""
def dataGeneration(argument):
    if(argument==3):
         laser_intensity= readPower()
    else:
        print("Please enter a correct argument")


def dataGeneration(argument, laser_intensity):
    if (argument==1):
        laser_intensity = laser_intensity+ laser_intensity*0.001*random()
    else:
        print("Please enter a correct argument")


def dataGeneration(argument, increment, fileName):
    if (argument==2):
        intensities = openRead(fileName)
        laser_intensity =intensities[increment]
    else:
        print("Please enter a correct argument")


def dataGeneration(argument, increment, fileArray):
    if (argument==2):
        laser_intensity =fileArray[increment]
    else:
        print("Please enter a correct argument")"""



#use the pandas library to read from a csv file containing the data
#Function tested and it works
def openReadCsv(fileName):
    data_file = pandas.read_csv(fileName, usecols=['intensity'])
    #print(data_file), show it writes in column
    intensities = data_file.intensity.to_list()
    return intensities
