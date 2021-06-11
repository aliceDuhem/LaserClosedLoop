#-----------------------------------------------------------------------------
def validation():
    if correct_entry_type(desiredPower.value)==True:
        if correct_entry_range_power(float(desiredPower.value))==True:
            outputValue=desiredPower.value
        else:
            outputValue= "Please enter a value in the range 0-10000"
    else:
        outputValue= "Please enter a number"

    if correct_entry_type(motorInc.value)==True:
        if correct_entry_range_increment(float(motorInc.value))==True:
            motorIncrement=motorInc.value
        else:
            motorIncrement= "Please enter a value in the range 0.001-2"
    else:
        motorIncrement= "Please enter a number"

    if correct_entry_type(HWPTrans.value)==True:
        if correct_entry_range_transmittance(float(HWPTrans.value))==True:
            HWPTransmittance=HWPTrans.value
        else:
            HWPTransmittance= "Please enter a value in the range 0-1"
    else:
        HWPTransmittance= "Please enter a number"

    if correct_entry_type(CubeTrans.value)==True:
        if correct_entry_range_transmittance(float(CubeTrans.value))==True:
            cubeTransmittance=CubeTrans.value
        else:
            cubeTransmittance= "Please enter a value in the range 0-1"
    else:
        cubeTransmittance= "Please enter the range"

    if (correct_entry_type(desiredPower.value)==True & correct_entry_range_power(float(desiredPower.value))==True)&(correct_entry_type(motorInc.value)==True&correct_entry_range_increment(float(motorInc.value))==True)&(correct_entry_type(HWPTrans.value)==True & correct_entry_range_transmittance(float(HWPTrans.value))==True)&(correct_entry_type(CubeTrans.value)==True & correct_entry_range_transmittance(float(CubeTrans.value))==True):
        textval = 'Entry validation:\nDesired Output = '+str(outputValue)+'W\n Motor Increment = '+str(motorIncrement)+'\nHalf Wave Plate Transmittance='+str(HWPTransmittance)+'\nCube Transmittance ='+str(cubeTransmittance)
        ValidationMessage.value=textval
        desiredPower.clear()
        motorInc.clear()
        HWPTrans.clear()
        CubeTrans.clear()



#Function that checks if the values is an float
def correct_entry_type(float_output):
    try:
        outputVal = float(float_output)
        return True
    except ValueError:
        print("Please enter a number")
        return False

#Function that checks if the values is in a correct range
def correct_entry_range_power(float_output):
    if (float_output >= MIN_VALUE_POWER) and (float_output <= MAX_VALUE_POWER):
        return True
    else:
        print("Please enter a value in the range 0-10000")
        return False

def correct_entry_range_increment(float_output):
    if (float_output >= MIN_INCREMENT) and (float_output <= MAX_INCREMENT):
        return True
    else:
        print("Please enter a value in the range 0.001-2")
        return False

def correct_entry_range_transmittance(float_output):
    if (float_output >= MIN_TRANSMITTANCE) and (float_output <= MAX_TRANSMITTANCE):
        return True
    else:
        print("Please enter a value in the range 0-1")
        return False

#-----------------------------------------------------------------------------
