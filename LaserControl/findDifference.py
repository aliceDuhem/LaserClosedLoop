
from ratioCodesv2 import ratio
from ratioCodesv2 import absolute
from ratioCodesv2 import difference
import random
import os
import datetime

# from general_characteristics import characteristics



#Definition of the functions
#-----------------------------------------------------------------------------

def createCsvFileData(data):
    motorIncrement =3333

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


#TODO: check motor range as dict only goes up to 45 deg. 
#TODO: implement code so that motor works up to 360 deg, 
#TODO: for angle > 90, (Angle % 90 - 45) = optimised angle (look into microstepping)

stepperIncrement=1       #motor increment, 0.9,1.8,... deg whatever the motor is

# laserIntensity = 1.2        #initial laser intensity
wantedIntensity =0.0009        # required intensity
Plaser_testVals = [0.00001,0.00005,0.00008,0.0001,0.00015,0.00016,0.00017,0.00018,0.00019,0.0002,0.0003,0.0004,0.0005,0.00055,0.00056,0.00057,0.00058,0.00059,0.0006,0.0007,0.0008,0.00085,0.00086,0.00087,0.00088,0.00089,0.0009,0.00095,0.001,0.0015,0.002,0.005]     # test values for fluctuating originla laser beam
motor_angle = 0  # current motor angle
Scaled_motor_angle = absolute.convAngle(motor_angle)        # convert current motor angle into 0-45, which is dictionary bounds
Pd_test = 1.05      # Current Pd laser detector test value

# Pc=[]
# Pd=[]
# Pi=[]

# # Calculates current Pc from Pd and Curent motor angle
print('If Pd =', Pd_test,'and Scaled_motor_angle =',Scaled_motor_angle, ' So Pc =',ratio.Pc_to_Pd(Scaled_motor_angle)*Pd_test,'\n') 


# # Calculates dictionary based of stepper motor increments, transmittance etc.
Dict = ratio.find_ratioDict(stepperIncrement)   
#prints the dictionary (ratio, increment angle)
print('Original Ratio for motor\n', Dict,'\n')

del Dict[0]

#multiply every key(ratio) in dict. by Pd, to find Pc according to angle
DictPc= {Pd_test/k:v for (k,v) in Dict.items()}
print('When Pd = ',Pd_test ,',The new Dict which shows the value of Pc at specific motor angles:\n',DictPc,'\n')

# Find the closest Pc value in new dict to wanted intensity. Angle would be printed which is the closest. 
# print('The angle which the motor needs to be at to acheive wanted intensity=',DictPc.get(wantedIntensity, DictPc[min(DictPc.keys(), key=lambda k:abs(k-wantedIntensity))]))




# TODO: closest angle would always be in between 0-45, have to convert back to angle which is closest to motor.
# EG. if motor is at 137 deg, and closest angle = 17deg. motor must move 26 deg to 163, instead of 30deg to 107 which is furthur even though it gives the same value. 
# Refer to ratio graph to visualise


## Test with difference code

# initial initialisation
#     -make dictionary from param of optical elements
#     - input wanted intensity

# Loop (try make function to do all these)
#     -find motor angle, Pd
#     -calculate Pc from ratio Pc, Pd
#     - multiply Pc with keys in origianl DIct, make new dict
#     - find wanted intensity from Dict, and output angle

data_array=[]

for i in Plaser_testVals:   
    print("\n----------Pd = ",i,"-----------------")
    print("ratio Pd/Pc,", ratio.Pc_to_Pd(motor_angle))
    print("Current Pc when Pd is the above,", absolute.Pc_from_Pd(i,motor_angle))
    print("Angle needed,",difference.neededAngle(motor_angle,i,stepperIncrement, wantedIntensity))
    # anglerotation =difference.neededAngle(motor_angle,i,stepperIncrement, wantedIntensity)
    # a=[i,anglerotation]
    # data_array.append(a)
    # print("New Pd / Pc ratio,", ratio.Pc_to_Pd(difference.neededAngle(motor_angle,i, stepperIncrement,wantedIntensity)))
# print(Dict.pop(0.0))
# print(Dict)
# createCsvFileData(data_array)


