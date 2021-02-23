
# Power on the RPi
# Ask the user for a power value (as area is constant and intensity is power*Area and we use the ratio)

# Rotate to 0

# Put the correct angle and remember the angle_motor

# Make the dictionary (for optical components)

#Loop:
    # Reads the value from the power PowerMeter
    # Make the new dictionary based on the Pd you have
    # Find Pc from measured Pd
    # Calculate the error from PC (entered-Pc computed)
    # Define a new target power (Calculated from PID: target = Pc*(error*Kp(PID coeff)+past_error*Kd+sum_past_error*Ki)
    # From target power, find new angle (with the second dictionary - same code as V.1 but change the wantyed Intensity)
    # Enters in the Pd to max code
    # Find the angle of intended rotation from target power
    # Send the angle to RPi (with GIPO-0)
    # Deconstruct the second dictionary
    # Write values in CSV (or in data array)
    # Write value on User GUI
#end of the loop

# Optionanl - send back to 0
# Write the values in CSV file for data analysis
# Destroy main DICTIONARY
# Shut RPi
