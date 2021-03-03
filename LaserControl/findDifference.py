
from ratioCodes import ratio
from ratioCodes import absolute
from ratioCodes import difference
import random
from general_characteristics import characteristics


#TODO: check motor range as dict only goes up to 45 deg. 
#TODO: implement code so that motor works up to 360 deg, 
#TODO: for angle > 90, (Angle % 90 - 45) = optimised angle (look into microstepping)

stepperIncrement=1       #motor increment, 0.9,1.8,... deg whatever the motor is

# laserIntensity = 1.2        #initial laser intensity
wantedIntensity =1          # required intensity
Plaser_testVals = [0.95, 0.9, 0.8,0.7,1.1,1.2,1.05]     # test values for fluctuating originla laser beam
motor_angle = 30      # current motor angle
Scaled_motor_angle = absolute.convAngle(motor_angle)        # convert current motor angle into 0-45, which is dictionary bounds
Pd_test = 0.1       # Current Pd laser detector test value

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

for i in Plaser_testVals:   
    print("----------Pd = ",i,"-----------------")
    print("ratio Pd/Pc,", ratio.Pc_to_Pd(motor_angle))
    print("Current Pc when Pd is the above,", absolute.Pc_from_Pd(i,motor_angle))
    print("Angle needed,",difference.neededAngle(motor_angle,i, wantedIntensity, Dict))
    print("New Pd / Pc ratio,", ratio.Pc_to_Pd(difference.neededAngle(motor_angle,i, wantedIntensity, Dict)))
# print(Dict.pop(0.0))
# print(Dict)


