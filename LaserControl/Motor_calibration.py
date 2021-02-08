##This function enbles to calibrate the motor when the device is first used

# read the intensity with the power meter. While the intensity is not the max, rotate by 1
#Could improve the speed ir by changing different values
#Max speed not needed as it is just for the initialisation

#TODO: Determine which direction increases pd and which decreases it
#TODO: instead of takin values from a array take it from the power meter

import os
from time import sleep

def motor_calibration():
    pd_max_value=0;
    reaction_time_Rpi = 10;

    while (readPower()>pd_max_value):
        #The power does not change when we read it as the plate has rotated already
        pd_max_value=readPower()
        #TODO: give to the raspberry Pi an angle to rotate from, take from function
        #Wait until the RPi has changed the angle of the half wave plate
        sleep(reaction_time_Rpi)
        #test
    else:
        #TODO: tell the raspberry Pi to go one step back (which should be max power meter value)
        print("The initialisation is finished")

def motor_calibration_array(array):
    pd_max_value=0;
    angle=0;
    min_angle_motor = 0.01;
    iterator = iter(array)
    p=next(iterator);

    while (p>pd_max_value):
        pd_max_value=p
        print(pd_max_value)
        p=next(iterator);
        #TODO: give to the raspberry Pi an angle to rotate from, take from function

        #test
        angle = min_angle_motor
        print(min_angle_motor)
    else:
        #TODO: tell the raspberry Pi to go one step back (which should be max power meter value)
        angle = -min_angle_motor
        print(angle)
        print("The initialisation is finished")

    return pd_max_value

motor_calibration_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 11.3, 10.5])
