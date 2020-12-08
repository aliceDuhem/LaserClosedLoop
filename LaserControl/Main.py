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


#Ask the user for the wanted intensity
#see code in App.py, will add later
#we get \/
outputValue
#Compute the error we authorise, so get outputValue_min and outputValue_max

#status_on tells if the program is shut or not, it is initially on so True
status_on = True;

while (status_on):
    #Find the power of the power_meter
    actual_power = print(power_meter.read)

    if actual_power<outputValue_max and actual_power>outputValue_min:
        sleep(TIME_BETWEEN_TWO_READINGS)
    else:
        #call the funciton that determines the angle that needs to be sent black
        #via a look up table
        sleep(ACTUATION_TIME)

    #put another function in for the status which checks the power meter is on
    #And throws an error if not, etc 
