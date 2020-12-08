#This part of the code compares the experimental value and the requested one

#outputValue refers to the requested value from the code App.py
#experimental_value refers to the value obtained from the power meter in GetPower.py

#The output of this part is an angle theta sent to the RPI

#Definition of the PID controller
#The values will need to be set with the formula
KP = 0.02
KD = 0.01
KI = 0.005
#This value is set by the user in the App.py
Target_power = outputValue #mW

power1_prev_error = 0
power1_sum_error = 0
angle = 0
a = 0 #a will be the factor by which we will multiply a power value to get the corresponding angle
# we still need to figure out what a actually is

while (status_on):
    power1_error = Target_power - power1.value
    power1 += (power1_error * KP) + (power1_prev_error * KD) + (power1_sum_error * KI)
    dtheta = a*power1 
    servo.angle = dtheta
    power1.reset()
    sleep(SAMPLETIME)
    power1_prev_error = power1_error
    power1_sum_error += power1_error
