import math


class getRatios:

    # converts ratio (Pc/Pd) csv file to python DICTIONARY
    # ensure the range is always 0 to 360 deg
    # output dict format = {'angle' : 'ratio' }


    def csv_to_ratio(fileName):

        #open file
        openedRatioFile = open(fileName) 

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

    def find_ratio(motor_increment, cube_transmittance=1, cube_reflectance=1):

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_increment = math.radians(motor_increment)
        #calculates amount of increments needed in range 0 to 360
        total_steps = math.pi *2 / motor_increment

        i=0
        ratio = {}


        while i < 2* math.pi:

            numerator = (cube_transmittance * math.sin(4*i + math.pi/2) +1) 
            denominator =  (cube_reflectance * math.sin(4*i -math.pi/2)+1)

            #check for inf values or 0
            if ((numerator ==0) or (denominator ==0)):
                fraction =0
            else:
                fraction = numerator / denominator

            #put angles and ratio into ductionary
            ratio[math.degrees(i)]=fraction
            i = i+motor_increment

        
        return ratio









