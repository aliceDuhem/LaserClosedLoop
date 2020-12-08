
#This first part cretaes the instrument we use
import visa
from ThorlabsPM100 import ThorlabsPM100
rm = visa.ResourceManager()
inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR',
                        term_chars='\n', timeout=1)
power_meter = ThorlabsPM100(inst=inst)

# These are commands, methods of the class
#print(power_meter.read) # Read-only property
#print(power_meter.sense.average.count) # read property
#power_meter.sense.average.count = 10 # write property, sense avg, 1 sample ~=3ms
#power_meter.system.beeper.immediate() # method, issues an audible signal
actual_power = print(power_meter.read) # Read-only property
