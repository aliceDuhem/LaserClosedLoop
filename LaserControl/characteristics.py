#Instead of writing the characteristcis in every function, we take them from this file

class Characteristics:

#TODO: get these characteristics from the GUI
    def __init__(self):
        self.stepperIncrement=0; # __makes the element private
        self.wantedPower=0; #get from GUI
        self.current_motor_angle=0;
        self.halfWave_transmittance=0;
        self.cube_ref_trans=1;
        self.cube_transmittance=0;
        #self.__diameter_beam=3; #in mm

    def setMotorAngle(self,motor_angle):
        self.current_motor_angle=motor_angle;

    def setIncrement(self,stepperIncrement):
        self.stepperIncrement=stepperIncrement;

    def setWantedPower(self,wantedPower):
        self.wantedPower=wantedPower;

    def setHTransmittance(self,halfWave_transmittance):
        self.halfWave_transmittance=halfWave_transmittance;

    def setCubeTransmittance(self,cube_transmittance):
        self.cube_ref_trans=1;
        self.cube_transmittance=cube_transmittance;

    def setWithPower(self,stepperIncrement,wantedPower,halfWave_transmittance,cube_transmittance):
        self.stepperIncrement=stepperIncrement; # __makes the element private
        self.wantedPower=wantedPower; #get from GUI
        self.current_motor_angle=0;
        self.halfWave_transmittance=halfWave_transmittance;
        self.cube_ref_trans=1;
        self.cube_transmittance=cube_transmittance;
        #self.__diameter_beam=3; #in mm
