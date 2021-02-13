#COntrol the motor with the library search, Without PID

import visa
from LaserControl.GetPower import PowerMeter
from guizero import App,Text,TextBox, PushButton

# power on the RPi
# Ask the user for a power value (as area is constant and intensity is power*Area and we use the ratio)

# Rotate to 0

# Put the correct angle and remember the angle_motor

# Make the dictionary (for optical components)

#Loop:
    # Reads the value from the power PowerMeter
    # Make the new dictionary based on the Pd you have
    # Enters in the Pd to max code 
    # Find the angle of intended rotation
    # Send the angle to RPi (with GIPO-0)
    # Deconstruct the second dictionary
    # Write values in CSV (or in data array)
#end of the loop

#Optionanl - send back to 0
#Write the values in CSV file for data analysis
#  destroy main DICTIONARY
# Shut RPi
