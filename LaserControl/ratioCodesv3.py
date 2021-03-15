import math
import sys

class ratio:

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

    def Plaser_from_Pd(Pd, motor_angle, cube_ref_trans=1, halfWave_transmittance =0.95):

        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        #ratio = 4* cube_ref_trans * halfWave_transmittance * pow(math.cos(motor_angle),2) * pow(math.sin(motor_angle),2)
        ratio = 0.5*cube_ref_trans * halfWave_transmittance * math.sin(4*motor_angle-math.pi/2) + (halfWave_transmittance*cube_ref_trans)/2
        return Pd*1/ratio



    #output ratio Pc / Pd at specific motor angle
    #Analytical solution version, better than Dict I think
    def Pc_to_Pd(motor_angle, cube_transmittance=0.95,cube_ref_trans=1):
         #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360


         # 45, 135, .. deg, Pc =0, Pd = Max
        if (motor_angle ==45 or motor_angle == 135 or motor_angle == 225 or motor_angle == 315):
                # Since ratio at angle 0 is inf, initialised MAXSIZE.
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
    def Pc_from_Pd(Pd, motor_angle, cube_transmittance=0.95, cube_ref_trans=0.95):

        denom =ratio.Pc_to_Pd(motor_angle, cube_transmittance,cube_ref_trans)

        if denom ==0:

            # return pm.readPower(pm.power_meter)
            # no power meter connected so run bottom
            return sys.maxsize

        return Pd * 1/denom


    #for angle > 90, (Angle % 90 - 45) = optimised angle
    #This code converts any angle to between 0 and 45
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

    def neededAngle(motor_angle,Pd, motorInc, wantedIntensity,cube_transmittance=0.95, cube_ref_trans=1, halfWave_transmittance =0.95):

        motor_angle=round(absolute.convAngle(motor_angle),2)

        Po=ratio.Plaser_from_Pd(Pd,motor_angle, cube_ref_trans, halfWave_transmittance)

        if wantedIntensity >=(Po*cube_transmittance*halfWave_transmittance):
            return 0

        cnum=2*wantedIntensity
        cdenum=Po*cube_transmittance*halfWave_transmittance
        c=cnum/cdenum
        c=c-1

        angle = math.degrees(((math.asin(c)*0.25+math.pi/8)))
        # invert angle graph
        angle=45-angle
        if angle%motorInc>(motorInc/2):
            closestVal=angle-angle%motorInc+motorInc
        else:
            closestVal=angle-angle%motorInc


        return closestVal