
#This first part cretaes the instrument we use
import visa
import pyvisa as visa
#import here the data from another power meter
from ThorlabsPM100 import ThorlabsPM100

#Write in the brackets what was imported
class PowerMeter:

#Method that create the power meter in the code
    def __init__(self):
        try:
            rm = visa.ResourceManager()
        except:
            print('Library visa not installed on the device')
        try:
            inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR',
                        term_chars='\n', timeout=1)
        except OSError:
            print('Cannot open ', 'USB0::0x0000::0x0000::xxxxxxxxx::INSTR')

        power_meter = ThorlabsPM100(inst=inst)

    def readPower(self):
        experimental_value = power_meter.read

#Tests
power = PowerMeter()
print(power.readPower())


# These are commands, methods of the class
# print(power_meter.read) # Read-only property
#print(power_meter.sense.average.count) # read property
#power_meter.sense.average.count = 10 # write property, sense avg, 1 sample ~=3ms
#power_meter.system.beeper.immediate() # method, issues an audible signal
#experimental_value = print(power_meter.read) # Read-only property
