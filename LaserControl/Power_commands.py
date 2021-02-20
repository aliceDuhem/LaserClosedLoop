# Install : python setup.py install

#Creates the createInstrumentimport visa
from ThorlabsPM100 import ThorlabsPM100
rm = visa.ResourceManager()
inst = rm.open_resource('USB0::0x0000::0x0000::xxxxxxxxx::INSTR',
                        term_chars='\n', timeout=1)
power_meter = ThorlabsPM100(inst=inst)

#Alternative, use usbtmc
from ThorlabsPM100 import ThorlabsPM100, USBTMC
inst = USBTMC(device="/dev/usbtmc0")
power_meter = ThorlabsPM100(inst=inst)

#All the commands
print power_meter.read # Read-only property
print power_meter.sense.average.count # read property
power_meter.sense.average.count = 10 # write property
power_meter.system.beeper.immediate() # method
