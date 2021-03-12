from ratioCodes import ratio
from ratioCodes import difference
from ratioCodes import absolute
from matplotlib import pyplot as plt

#Plot the ratio versus the angle
stepperIncrement=0.2
HWPTransmittance = 0.95
cubeTransmittance = 0.95
cubeRefTransmittance=1
motor_angle = 0
Scaled_motor_angle = absolute.convAngle(motor_angle)        # convert current motor angle into 0-45, which is dictionary bounds

ratio_dict = ratio.find_ratioDict(stepperIncrement,cubeTransmittance,cubeRefTransmittance)
#del ratio_dict[0]
y,x=zip(*ratio_dict.items()) #Puts dictionary into a ratioList

#plt.plot(x,y)
#plt.xlabel('Angle')
#plt.ylabel('Ratio Pc/Pd')
#plt.title('Ratio Pc/Pd with respect to the Half Wave Plate angle')
#plt.show()


#Plot Pc at different angles
motor_angle=0
Pd=0.00045
AngleArray = []
PcArray = []
while motor_angle<45:
    AngleArray.append(motor_angle)
    PcArray.append(absolute.Pc_from_Pd(Pd,motor_angle,cubeTransmittance,cubeRefTransmittance))
    motor_angle=motor_angle+stepperIncrement

plt.plot(AngleArray,PcArray)
plt.xlabel('Angle')
plt.ylabel('Pc')
plt.title('Value of Pc computed with varying HWP angle when the Pd is 0.45mW')
plt.show()


#Plot Pc at different Pd same angle
motor_angle=80
Pd=0
PdArray = []
PcArray = []
while Pd<0.9:
    PdArray.append(Pd)
    PcArray.append(absolute.Pc_from_Pd(Pd,motor_angle,cubeTransmittance,cubeRefTransmittance))
    Pd=Pd+0.01

#plt.plot(PdArray,PcArray)
#plt.xlabel('Pd')
#plt.ylabel('Pc')
#plt.title('Value of Pc computed with varying Pd when the HWP angle is 80')
#plt.show()
