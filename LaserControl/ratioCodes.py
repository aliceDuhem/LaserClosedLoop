import math

#this class contains functions which output a ratio
class ratio:

    # converts ratio (Pc/Pd) csv file to python DICTIONARY
    # ensure the range is always 0 to 360 deg
    # output dict format = {'angle' : 'ratio' }


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
                ratio_dict[element] = ratioList[element]

        return ratio_dict






    # makes Dictionary of angle and ratio based of motor increments
    # output angles would be from 0 to 360 deg
    # output dict format = {'angle' : 'ratio' }
    #motor increment must be in DEG

    def find_ratioDict(motor_increment, cube_transmittance=1, cube_ref_trans=1):

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_increment = math.radians(motor_increment)
        #calculates amount of increments needed in range 0 to 360
        total_steps = math.pi *2 / motor_increment

        i=0
        ratio = {}


        while i < 2* math.pi:

            numerator = (cube_transmittance * math.sin(4*i + math.pi/2) +1) 
            denominator =  (cube_ref_trans * math.sin(4*i -math.pi/2)+1)

            #check for inf values or 0
            if ((numerator ==0) or (denominator ==0)):
                fraction =0
            else:
                fraction = numerator / denominator

            #put angles and ratio into ductionary
            ratio[math.degrees(i)]=fraction
            i = i+motor_increment

        
        return ratio



    #Ratio Pc / Plaser
    def Pc_to_Plaser(motor_angle, cube_transmittance=1, halfWave_transmittance =1):
        
        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        ratio = cube_transmittance * halfWave_transmittance *(math.cos(motor_angle)^2 - math.sin(motor_angle)^2)^2

        return ratio




    #ratio Pd / Plaser
    def Pd_to_Plaser(motor_angle, cube_ref_trans=1, halfWave_transmittance =1):
        
        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        ratio = 4* cube_ref_trans * halfWave_transmittance * math.cos(motor_angle)^2 * math.sin(motor_angle)^2
        
        return ratio



    #ratio Pc / Pd
    #Analytical solution version, better than Dict I think
    def Pc_to_Pd(motor_angle, cube_transmittance=1,cube_ref_trans=1):

         #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360


         # 45, 135, .. deg, Pc =0, Pd = Max
        if (motor_angle ==45 or motor_angle == 135 or motor_angle == 225 or motor_angle == 315):
            return 0

        # TODO:  find a way to find max instataneous power variation
        # 0, 90, ..., deg, Pc = Max, Pd = 0
        if (motor_angle == 0 or motor_angle%90==0):
            return 0

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        numerator = (cube_transmittance * math.sin(4*motor_angle + math.pi/2) +1) 
        denominator =  (cube_ref_trans * math.sin(4*motor_angle -math.pi/2)+1)

        ratio = numerator/denominator

        return ratio





#class with functions which output finished values, eg. Pc Pd
#these functions do not output ratios
class absolute:



     #function to find instataneous Pc given angles and other variables
    def Pc_from_Pd(Pd, motor_angle, cube_transmittance=1, cube_ref_trans=1):

        return Pd * ratio.Pc_to_Pd(motor_angle, cube_transmittance,cube_ref_trans)


