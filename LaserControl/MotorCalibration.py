##This function enbles to calibrate the motor when the device is first used

# read the intensity with the power meter. While the intensity is not the max, rotate by 1
#Could improve the speed ir by changing different values
#Max speed not needed as it is just for the initialisation

#TODO: Determine which direction increases pd and which decreases it
#TODO: instead of takin values from a array take it from the power meter

import os
from time import sleep
from GetPower import PowerMeter

class Calibration:

    def motor_to_0(pm):
        pd_max_value=0
        #TODO: Compute reaction time RPi
        reaction_time_Rpi = 10

        while (pm.readPower()>pd_max_value):
            #The power does not change when we read it as the plate has rotated already
            pd_max_value=pm.readPower()
            #TODO: give to the raspberry Pi an angle to rotate from, take from function
            #ROTATE BY 1 STEP
            #Wait until the RPi has changed the angle of the half wave plate
            sleep(reaction_time_Rpi)
        else:
            #TODO: tell the raspberry Pi to go one step back (which should be max power meter value)
            print("The initialisation is finished")

    def motor_to_initial_power(pm,wantedPower,motorIncrement,cubeTransmittance,cubeRefTransmittance,HWPTransmittance):
        # Set up the power meter and Dictionnary
        #---------------------------------------------------------------------------
        #the time the signal takes to go from the code to the RPi
        reaction_time_Rpi = 10
        # current motor angle, after calibration
        current_motor_angle = 0

        #inst_power = pm.readPower();
        inst_power=1;

        # Calculates dictionary based of stepper motor increments, transmittance etc.
        #oriDictionary = ratio.find_ratioDict(motorIncrement)

        #Angle at which the motor needs to be at to achieve the wanted intensity
        additional_angle = difference.neededAngle(current_motor_angle, inst_power,motorIncrement,wantedPower,cubeTransmittance,cubeRefTransmittance,HWPTransmittance)

        #The new angle is the previous one + the angle by which the motor turns
        current_motor_angle=current_motor_angle+additional_angle
        #TODO: enter the function that sends the code to the Rpi
        return current_motor_angle


    #Tests the code when we don't have the power meter connected to it (using arrays)
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

    #motor_calibration_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 11.3, 10.5])
