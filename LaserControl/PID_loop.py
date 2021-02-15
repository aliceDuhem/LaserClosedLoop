
from time import sleep
from gpiozero import Motor
import App.Py
import dataGenerationScript.py
import GetPower.py

#Here we would add the function that calibrates the plate to have initial angle of 0
def PID(KP,KD,KI,oriDictionary,SAMPLETIME):

    #SAMPLETIME = 1 #need to find an actual value for this
    #KP = 0.02
    #KD = 0.01
    #KI = 0.005

    motor = Motor(f=3, b=14)  # Pin numbers I found as an example on the internet, will need to verify

    Target_power = float_output # from App.Py
    #power1_vector = dataGeneration(argument=1,laser_intensity=Target_power,increment=1,fileArray=1) #Not sure how to use this function...
    # Comes from the computer
    power1_prev_error = 0 #if we are already using the PID function in a loop in the main script, we should initiate these in the main and not in the function
    power1_sum_error = 0
    angle = 0
    step_angle = 1.8  # angle turned by the motor in one step: need to find out the real value

    while True:
        power1 = readPower()
        power1_error = Target_power - power1.value
        power1 += (power1_error * KP) + (power1_prev_error * KD) + (power1_sum_error * KI)
        Pd = Pc_to_Pd(angle, cube_transmittance = 1, cube_ref_trans = 1)
        dtheta = neededAngle(angle,Pd, power1, oriDictionary)
        step_nb = dtheta // step_angle  # number of steps the motor will make to turn to the desired angled
        for i in range(step_nb):
            motor.forward()
        power1.reset()
        sleep(SAMPLETIME)
        power1_prev_error = power1_error
        power1_sum_error += power1_error
        angle = step_nb * step_angle


