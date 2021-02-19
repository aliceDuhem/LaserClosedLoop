from guizero import App,Text,TextBox, PushButton
#-----------------------------------------------------------------------------
#Constant values
MIN_VALUE_POWER=0
MAX_VALUE_POWER=10000
MIN_TRANSMITTANCE=0
MAX_TRANSMITTANCE=1
MIN_INCREMENT=0.000001
MAX_INCREMENT=4

#-----------------------------------------------------------------------------
def validation():
    if correct_entry_type(desiredPower.value)==True:
        if correct_entry_range_power(float(desiredPower.value))==True:
            outputValue.value=desiredPower.value
        else:
            outputValue.value= "Please enter a value in the range 0-10000"
    else:
        outputValue.value= "Please enter a number"

    if correct_entry_type(motorInc.value)==True:
        if correct_entry_range_increment(float(motorInc.value))==True:
            motorIncrement.value=motorInc.value
        else:
            motorIncrement.value= "Please enter a value in the range 0.001-2"
    else:
        motorIncrement.value= "Please enter a number"

    if correct_entry_type(HWPTrans.value)==True:
        if correct_entry_range_transmittance(float(HWPTrans.value))==True:
            HWPTransmittance.value=HWPTrans.value
        else:
            HWPTransmittance.value= "Please enter a value in the range 0-1"
    else:
        HWPTransmittance.value= "Please enter a number"

    if correct_entry_type(CubeTrans.value)==True:
        if correct_entry_range_transmittance(float(CubeTrans.value))==True:
            cubeTransmittance.value=CubeTrans.value
        else:
            cubeTransmittance.value= "Please enter a value in the range 0-1"
    else:
        cubeTransmittance.value= "Please enter the range"

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

#App Display
app= App(title="Closed Loop Laser Intensity Regulator")
welcomeMessage = Text(app,text="Welcome to the Closed Loop Laser intensity regulator software",
                      size=30,color='black')
boxPowerMessage=Text(app,text="Enter the desired laser output power")
#Textbox where the user enters the desired power
desiredPower=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxIncMessage=Text(app,text="Enter the motor Increment")
#Textbox where the user enters the desired power
motorInc=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxHWPMessage=Text(app,text="Enter the half wave plate transmittance")
#Textbox where the user enters the desired power
HWPTrans=TextBox(app,width=50,height=10)

blank=Text(app,text="")

boxCubeMessage=Text(app,text="Enter the cube transmittance")
#Textbox where the user enters the desired power
CubeTrans=TextBox(app,width=50,height=10)

blank=Text(app,text="")

#Button that validates the entry and stores the textbox value as desired output
validation=PushButton(app,command=validation,text="Validate Entry")

app.display()