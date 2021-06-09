import pyvisa as visa
#If necessary, import here the data from another power meter
from ThorlabsPM100 import ThorlabsPM100


class PowerMeter:

#Method that create the power meter in the code
    def __init__(self):
        try:
            rm = visa.ResourceManager()
        except:
            print('Library visa not installed on the device')
        try:
            #Gets the port where the power meter is
            usb_port = rm.list_resources()
            print(rm.list_resources())
            usb_port_str=str(usb_port)
            usb='';
            for i in range (2,39):
                usb = usb+usb_port_str[i]
            print(usb)

            #Value read from the previous command
            #Otherwise write in the form 'USB0::0x0000::0x0000::xxxxxxxx::INSTR'
            inst = rm.open_resource(usb)
        except OSError:
            print('Cannot open ', usb)

        #Creates in the class an instance of the power meter
        self.power_meter = ThorlabsPM100(inst=inst)

    #Reads the power at a given time
    def readPower(self,power_meter):
        experimental_value = power_meter.read
        return experimental_value

#Tests and how to use the code

#power = PowerMeter()
#print(power.readPower(power.power_meter))


# These are commands, methods of the class
""" print(power_meter.read) # Read-only property
print(power_meter.sense.average.count) # read property
power_meter.sense.average.count = 10 # write property, sense avg, 1 sample ~=3ms
power_meter.system.beeper.immediate() # method, issues an audible signal
experimental_value = print(power_meter.read) # Read-only property"""
