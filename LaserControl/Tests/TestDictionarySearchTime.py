#This code tests ho long it takes to look for 1000 different data in the DICTIONARY
#It is a way to deduce if the library is sufficient for our system (or if PID is needed)

#Imports the required functions and files for the test
import time
from ratioCodes import ratio
from ratioCodes import absolute
from ratioCodes import difference
import Wing_findDifference
import dataGenerationScript
import SaveDataCsv

stepperIncrement=0.45       #motor increment, 0.9,1.8,... deg whatever the motor is
laserIntensity = 8.20        #initial laser intensity (W/cm^2)
wantedIntensity =8.37          # required intensity
motor_angle = 80       # current motor angle
Scaled_motor_angle = absolute.convAngle(motor_angle)        # convert current motor angle into 0-45, which is dictionary bounds
Pd_test=1.2             #gets the initial power at d (towards power meter)

#Saves the data
data=[]

# Calculates dictionary based of stepper motor increments, transmittance etc.
Dict = ratio.find_ratioDict(stepperIncrement)


t0 =time.time()

#test 1: use the case 1 of data generator
for i in range(1000) :
    #Find the value for Pd from the loop
    # Find the closest Pc value in new dict to wanted intensity. Angle would be printed which is the closest.
    DictPc= {k*Pd_test:v for (k,v) in Dict.items()}
    angle_motor = DictPc.get(wantedIntensity, DictPc[min(DictPc.keys(), key=lambda k:abs(k-wantedIntensity))])
    row=[SaveDataCsv.datetime.datetime.now(),Pd_test,angle_motor]
    data.append(row)
    Pd_test = dataGenerationScript.dataGeneration(1,Pd_test,0,"")


t1=time.time()
v1_time = t1-t0

SaveDataCsv.createCsvFileData(data)

print("Time for the dictionary search for 1000 values with random data generation type 1: ",v1_time)

#test 2: use the case 2 of data generator: read from CSV file (can mimic the time to get from )

fileName = "intensity_readings_second_2021-Jan-31_19-38-54.csv"
#gets the intensity column, 1000 data
data_intensities=dataGenerationScript.openReadCsv(fileName)

t2 =time.time()
for i in range(1000) :
    #gets the pd from the csv file (column of data)
    Pd_test = dataGenerationScript.dataGeneration(2,0,i,data_intensities)
    #Find the value for Pd from the loop
    # Find the closest Pc value in new dict to wanted intensity. Angle would be printed which is the closest.
    DictPc= {k*Pd_test:v for (k,v) in Dict.items()}
    angle_motor = DictPc.get(wantedIntensity, DictPc[min(DictPc.keys(), key=lambda k:abs(k-wantedIntensity))])
    row=[SaveDataCsv.datetime.datetime.now(),Pd_test,angle_motor]
    data.append(row)

t3=time.time()
v2_time = t3-t2

print("Time for the dictionary search for 1000 values from csv file: ",v2_time)
