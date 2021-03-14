
from ratioCodesv2 import ratio
from ratioCodesv2 import absolute
from ratioCodesv2 import difference
import random

# from general_characteristics import characteristics


#TODO: check motor range as dict only goes up to 45 deg. 
#TODO: implement code so that motor works up to 360 deg, 
#TODO: for angle > 90, (Angle % 90 - 45) = optimised angle (look into microstepping)

stepperIncrement=1       #motor increment, 0.9,1.8,... deg whatever the motor is

# laserIntensity = 1.2        #initial laser intensity
wantedIntensity =0.0009        # required intensity
Plaser_testVals = [0.00001,0.00005,0.00008,0.0001,0.00015,0.00016,0.00017,0.00018,0.00019,0.0002,0.0003,0.0004,0.0005,0.00055,0.00056,0.00057,0.00058,0.00059,0.0006,0.0007,0.0008,0.00085,0.00086,0.00087,0.00088,0.00089,0.0009,0.00095,0.001,0.0015,0.002,0.005]     # test values for fluctuating originla laser beam
motor_angle = 30  # current motor angle
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
    anglerotation =difference.neededAngle(motor_angle,i,stepperIncrement, wantedIntensity)
    a=[i,anglerotation]
    data_array.append(a)
    # print("New Pd / Pc ratio,", ratio.Pc_to_Pd(difference.neededAngle(motor_angle,i, stepperIncrement,wantedIntensity)))
# print(Dict.pop(0.0))
# print(Dict)
createCsvFileData(data_array)


