# This code represents the main of the program
# It includes:
# The class that gets the power from the power_meter
# The class that displays that ask the power from the user
# The class that compares the values and comes up with an output angle
# The class that sends the output to the RaspberryPi for actuation

#-------------------------------------------------------------------------------
#All the libraries used int the code (visa, Thorlabs, guizero)

#libraries for the power meter
import visa
from ThorlabsPM100 import ThorlabsPM100
#libraries for the app display
from guizero import App,Text,TextBox, PushButton
#-------------------------------------------------------------------------------

#All the constant values required in the code

#%error tolerated regarding the intensity
ERROR = 0.05
#The time between two readings in ms
TIME_BETWEEN_TWO_READINGS = 1000
#actuation time after which reading is taken, need to determine experimentaly
ACTUATION_TIME = 100

#-------------------------------------------------------------------------------
#Start by creating the power meter  using VISA
rm = visa.ResourceManager()
inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR',
                        term_chars='\n', timeout=1)
power_meter = ThorlabsPM100(inst=inst)


#-------------------------------------------------------------------------------
#Ask the user for the wanted intensity
#see code in App.py, will add later
#we get \/
outputValue

#This value is set by the user in the App.py
Target_power = outputValue
#Compute the error we authorise, so get outputValue_min and outputValue_max
#-------------------------------------------------------------------------------
#Definition of the PID controller
#The values will need to be set with the formula
KP = 0.02
KD = 0.01
KI = 0.005

power1_prev_error = 0
power1_sum_error = 0
angle = 0
a = 0 #a will be the factor by which we will multiply a power value to get the corresponding angle
# we still need to figure out what a actually is
# This shuld call a lookup table

#-------------------------------------------------------------------------------
#status_on tells if the program is shut or not, it is initially on so True
#TODO: create a status function
status_on = True;

while (status_on):
    #Get the power of the power_meter
    actual_power = print(power_meter.read)

    power1_error = Target_power - actual_power.value
    actual_power += (power1_error * KP) + (power1_prev_error * KD) + (power1_sum_error * KI)
    dtheta = a*power1

    power1_prev_error = power1_error
    power1_sum_error += power1_error
    power1.reset()
    sleep(ACTUATION_TIME)


    #This is another way I thought of doing it, tell me which one you prefer
    # experimental_power = print(power_meter.read)
    # power1_error = Target_power - experimental_power.value

    # if power1_error>ERROR:
        # experimental_power += (power1_error * KP) + (power1_prev_error * KD) + (power1_sum_error * KI)
        # dtheta = a*power1
        #TODO: USE A FTP TO SEND DTHETA TO THE RPI
        # power1_prev_error = power1_error
        # power1_sum_error += power1_error
        # sleep(ACTUATION_TIME)
    # else:
        # sleep(TIME_BETWEEN_TWO_READINGS)


    #TODO: put another function in for the status which checks the power meter is on
    #And throws an error if not, etc
