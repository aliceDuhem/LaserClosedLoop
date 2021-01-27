from ratioCodes import ratio
from ratioCodes import absolute



#TODO: check motor range as dict only goes up to 45 deg. 
#TODO: implement code so that motor works up to 360 deg, 
#TODO: for angle > 90, (Angle % 90 - 45) = optimised angle

stepperIncrement=0.45
laserIntensity = 1.2
wantedIntensity =1
Plaser_testVals = [0.95, 0.9, 0.8,0.7,1.1,1.2,1.05]
motor_angle = 168
Scaled_motor_angle = absolute.convAngle(motor_angle)
Pd_test = 0.5

Pc=[]
Pd=[]
Pi=[]

print('If Pd = ', Pd_test,'and Scaled_motor_angle = ',Scaled_motor_angle, 'Pc = ',ratio.Pc_to_Pd(Scaled_motor_angle)*Pd_test)  #Find Pc at specific motor angle

Dict = ratio.find_ratioDict(stepperIncrement)   #Make Dict for stepper motor increment
print('Ratio for motor', Dict)

#multiply every key in dict. by Pd, to find Pc according to angle
Dict1= {k*Pd_test:v for (k,v) in Dict.items()}
print('Pc Dict when Pd =',Dict1)

#get closest angle to wantedIntensity
print('closestAngle=',Dict1.get(wantedIntensity, Dict1[min(Dict1.keys(), key=lambda k:abs(k-wantedIntensity))]))




# print(Pc)
# print(Pi)
# print(Pd_test)






