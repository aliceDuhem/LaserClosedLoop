import math
import sys


class ratio:
    def Plaser_from_Pd(Pd, motor_angle, cube_ref_trans=0.95, halfWave_transmittance =0.9):

        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        #ratio = 4* cube_ref_trans * halfWave_transmittance * pow(math.cos(motor_angle),2) * pow(math.sin(motor_angle),2)
        ratio = 0.5*cube_ref_trans * halfWave_transmittance * math.sin(4*motor_angle-math.pi/2) + (halfWave_transmittance)/2
        return Pd*1/ratio

    def Pc_from_Pd(Pd, motor_angle, cube_ref_trans=0.95,cube_trans=0.9, halfWave_transmittance =0.9):
        #Convert angles to 0<angle<360
        if motor_angle>360:
            motor_angle = motor_angle%360

        #trig in math module works in RAD, convert motor increenet in degrees to rad
        motor_angle = math.radians(motor_angle)

        #First find Plaser
        Po=Plaser_from_Pd(Pd, motor_angle, cube_ref_trans, halfWave_transmittance)

        #ratio = 4* cube_ref_trans * halfWave_transmittance * pow(math.cos(motor_angle),2) * pow(math.sin(motor_angle),2)
        Pc= 0.5*Po*(halfWave_transmittance*cube_trans* math.sin(4*motor_angle+math.pi/2) + (halfWave_transmittance))
        return Pc


#class with functions which output absolute values, eg. Pc Pd
#these functions do not output ratios
class absolute:

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

    def neededAngle(motor_angle,Pd, motorInc, wantedIntensity,cube_transmittance, cube_ref_trans, halfWave_transmittance):

        motor_angle=round(absolute.convAngle(motor_angle),2)

        Po=ratio.Plaser_from_Pd(Pd,motor_angle, cube_ref_trans, halfWave_transmittance)

        if wantedIntensity >=(Po*cube_transmittance*halfWave_transmittance):
            return 0

        cnum=2*wantedIntensity
        cdenum=Po*cube_transmittance*halfWave_transmittance
        c=cnum/cdenum
        c=c-(1/cube_transmittance)

        angle = math.degrees(((math.asin(c)*0.25-math.pi/8)))

        # invert angle graph (might change 45 to 90 if not working as it repeats every 45 to 90 deg, i'm still unsure)
        angle=45-angle
        if angle%motorInc>(motorInc/2):
            closestVal=angle-angle%motorInc+motorInc
        else:
            closestVal=angle-angle%motorInc


        return closestVal
