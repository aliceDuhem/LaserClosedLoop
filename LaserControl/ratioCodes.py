import math
import sys
from typing import OrderedDict
# from GetPower import PowerMeter



#inputs float
#this class contains functions which output a ratio
class ratio:

    # converts ratio (Pc/Pd) csv file to python DICTIONARY
    # ensure the range is always 0 to 360 deg
    # output dict format = {'ratio' : 'angle' }
    # creates Dict from 0 to 45, optimisation, dict repeats

    def csv_to_ratioDict(fileName):

        #open file
        openedRatioFile = open(fileName) 
        if openedRatioFile:
            1
        else:
            print('File cannot be opened')
            return -1

        #initialise empty dictionary
        ratio_dict = {}


        for line in openedRatioFile:
            ratioList = line.split(",")
            for element in range(len(ratioList)):
                #add angle and ratio to dictionary
                if element<45.0000001:
                    ratio_dict[ratioList[element]] = element
                
        return ratio_dict






    # makes Dictionary of angle and ratio based of motor increments
    # output angles would be from 0 to 360 deg
    # output dict format = {'ratio' : 'angle' }
    # motor increment must be in DEG
    # DICT created only goes from 0 to 45, optimisation, repetiition
    # Since ratio at angle 0 is inf, initialised MAXSIZE. 

    def find_ratioDict(motor_increment, cube_transmittance=1, cube_ref_trans=1):

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_increment = math.radians(motor_increment)
        #calculates amount of increments needed in range 0 to 360
        total_steps = math.pi *2 / motor_increment

        i=0
        ratio = {}

        # run i to make doctionary from angle 0 to 45 deg.
        while i <= 0.25* math.pi + 0.0001:

            denominator = (cube_transmittance * math.sin(4*i + math.pi/2) +1) 
            numerator =  (cube_ref_trans * math.sin(4*i -math.pi/2)+1)

            #check for inf values or 0
            if (numerator ==0):
                fraction =0
            elif (denominator ==0):
                fraction = sys.maxsize
            else:
                fraction = numerator / denominator

            #put angles and ratio into ductionary
            ratio[fraction]=round(math.degrees(i),2)
            i = i+motor_increment

        return ratio



    #output Ratio Pc / Plaser
    def Pc_to_Plaser(motor_angle, cube_transmittance=1, halfWave_transmittance =1):
        
        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        ratio = cube_transmittance * halfWave_transmittance *pow((pow(math.cos(motor_angle),2) - pow(math.sin(motor_angle),2)),2)

        return ratio




    #output ratio Pd / Plaser
    def Pd_to_Plaser(motor_angle, cube_ref_trans=1, halfWave_transmittance =1):
        
        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        ratio = 4* cube_ref_trans * halfWave_transmittance * pow(math.cos(motor_angle),2) * pow(math.sin(motor_angle),2)
        
        return ratio



    #output ratio Pc / Pd at specific motor angle
    #Analytical solution version, better than Dict I think
    def Pc_to_Pd(motor_angle, cube_transmittance=1,cube_ref_trans=1):
         #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360


         # 45, 135, .. deg, Pc =0, Pd = Max
        if (motor_angle ==45 or motor_angle == 135 or motor_angle == 225 or motor_angle == 315):
            return sys.maxsize  #after inversion pd/pc

        # TODO:  find a way to find max instataneous power variation
        # 0, 90, ..., deg, Pc = Max, Pd = 0
        if (motor_angle == 0 or motor_angle%90==0):
            return 0

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        denominator = (cube_transmittance * math.sin(4*motor_angle + math.pi/2) +1) 
        numerator =  (cube_ref_trans * math.sin(4*motor_angle -math.pi/2)+1)

        ratio = numerator/denominator

        return ratio





#class with functions which output absolute values, eg. Pc Pd
#these functions do not output ratios
class absolute:



     #function to find instataneous Pc at specific angle
    def Pc_from_Pd(Pd, motor_angle, cube_transmittance=1, cube_ref_trans=1):

        denom =ratio.Pc_to_Pd(motor_angle, cube_transmittance,cube_ref_trans)
        
        if denom ==0:

            # return pm.readPower(pm.power_meter)
            # no power meter connected so run bottom
            return sys.maxsize

        return Pd * 1/denom




    #TODO: check motor range as dict only goes up to 45 deg. 
    #TODO: implement code so that motor works up to 360 deg, 
    #for angle > 90, (Angle % 90 - 45) = optimised angle
    #This code converts any angle to between 0 and 45
    #This allows the angle to be mapped onto the optimised DICT
    def convAngle( angle):
        angle=abs(angle)
        if angle > 90:
            angle = angle % 90
            if angle > 45:
                angle=90-angle
            return angle
        if angle > 45:
            angle=90-angle
        return angle

        


class difference:

    # Outputs Angle needed for wanted intensity at specific Pd
    # Run to find new Pc everytime because Pd would change according to laser fluctuations
    # def neededAngle(motor_angle,Pd, wantedIntensity, oriDictionary):

    def neededAngle(motor_angle,Pd, wantedIntensity, oriDictionary):
        

        #scale motor angle
        motor_angle=round(absolute.convAngle(motor_angle),2)
        # print(Pd/ratio.Pc_to_Pd(motor_angle))
        #multiply every value in original Dict with Pd to see how Pc varies with motor angle
        DictPc={Pd/k:v for (k,v) in oriDictionary.items() }
        #DictPc is just theoretical Pc values at every single angle, it does not take into account limits such as max input value and so on
        
        # check if calculated(wanted) Pc is more than total intensity (Pc +Pd), if True give max power, deg=0
        # IGNORE LINE-->: cannot use Pd as we need to kmow (somewhat) the definate max power, and Pd does not give us a clue
        if ( wantedIntensity > Pd/ratio.Pc_to_Pd(motor_angle) +Pd):
            return 0

        # handle exception where Pd = Pc at 45 deg
        if motor_angle ==45:

            # at instant 45 deg, Pc at 0deg would be the max value, max value in this case is power meter reading
            # as at 45 deg all the power goes to the detector, code at the bottom with getpower solves this
            zeros = {Pd:0.0}

            # use bottom when connected to power meter
            # zeros = {pm.readPower(pm.power_meter):0.0}

            DictPc.update(zeros)

            # delete keys which is more than wanted intensity at 45 deg so prog would return 0 and give max power instead
            for key in list(DictPc.keys()):
                if key > Pd:
                    del DictPc[key]



        # elif motor_angle ==0:
            # original power of laser, no way of detecting it as no power goes to the detector

        else:
            # Must delete 0 before putting dict into function
            # add zeros as key and val after devision because python cannot deal with 0's
            zeros = {sys.maxsize:0.0}
            DictPc.update(zeros)


        #sort dictionary by key, so at 45 deg {Pd:0} would appear before the others and prog would choose that instead
        DictPc = OrderedDict(sorted(DictPc.items()))

        # print(DictPc)

        # Find the closest value Pc to wanted intensity from Dict, when system is
        # at the specific Pd
        closestVal = DictPc.get(wantedIntensity, DictPc[min(DictPc.keys(), key=lambda k:abs(k-wantedIntensity))])
        # print(Pd/ratio.Pc_to_Pd(closestVal) +Pd)

        if closestVal ==0:
            # print("UUUUUUU")
            return 0



        del DictPc
        return closestVal


        

