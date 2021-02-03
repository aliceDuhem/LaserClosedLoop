## this code would run in the raspberry pi console since it uses libraries specific to RPI
## I need to check how importing libraries works with serial communication between PI and the other codes

from time import sleep
from gpiozero import Motor
import App.Py
import threading
import dataGenerationScript.py

#Here we would add the function that calibrates the plate to have initial angle of 0

SAMPLETIME = 1 #need to find an actual value for this

motor = Motor(f=3, b=14) #Pin numbers I found as an example on the internet, will need to verify

# For the moment these are random coefficients
KP = 0.02
KD = 0.01
KI = 0.005

Target_power = float_output # from App.Py
power1_vector = dataGeneration(argument=1,laser_intensity=Target_power,increment=1,fileArray=1) #Not sure how to use this function...
power
# Comes from the computer
power1_prev_error = 0
power1_sum_error = 0
angle = 0 # will get this from Wings code I guess
step_angle = 1.8  # angle turned by the motor in one step: need to find out the real value

while True:
    power1_error = Target_power - power1.value
    power1 += (power1_error * KP) + (power1_prev_error * KD) + (power1_sum_error * KI)
    dtheta = find_angle(power1,angle) ##find_angle would be Wings function...I can always change this part
    step_nb = dtheta // step_angle  # number of steps the motor will make to turn to the desired angled
    for i in range(step_nb):
        motor.forward()
    power1.reset()
    sleep(SAMPLETIME)
    power1_prev_error = power1_error
    power1_sum_error += power1_error
    angle = dtheta #Not sure this is true, is dtheta the optimal angle or the closest possible angle to the optimal one?

#Here we would add the function that resets the angle to 0 at the end

