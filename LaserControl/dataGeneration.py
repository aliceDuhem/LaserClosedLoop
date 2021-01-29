import pandas
import os

#Generates intensity data to test the code
#Asks for the type of data generation - the increment it is at (first or last data)#
# And if it is case 2, gets the file name to open it
def dataGeneration(argument,increment,fileArray):

    #This case gives back a random data depending on the previous one
    if (argument==1):
        laser_intensity = laser_intensity*0.005+increment

    #This case reads from a file
    elif (argument==2):
        intensities = openRead(fileName)
        print(intensities[0])
        #do nothing yet

    #This case will be implemented, it takes the data from the powermeter
    elif(argument==3):
         laser_intensity= readPower()

    else:
        print("Please enter a correct argument")

#use the pandas library to read from a csv file containing the data
def openReadCsv(fileName):
    data_file = pandas.read_csv(fileName, usecols=['intensity'])
    #print(data_file), show it writes in column
    intensities = data_file.intensity.to_list()
    return intensities

#Try the openReadCsv funciton
intensities = openReadCsv(fileName)
print(intensities[0])
