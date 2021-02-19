#Instead of writing the characteristcis in every function, we take them from this file

class Characteristics:

#TODO: get these characteristics from the GUI
    def __init__(self,stepperIncrement,wantedIntensity,current_motor_angle,halfWave_transmittance,cube_ref_trans,cube_transmittance,diameter_beam):
        self.__stepperIncrement=0.45; # __makes the element private
        self.__wantedIntensity=0; #get from GUI
        self.__current_motor_angle=0;
        self.__halfWave_transmittance=1;
        self.__cube_ref_trans=1;
        self.__cube_transmittance=1;
        self.__diameter_beam=3; #in mm
