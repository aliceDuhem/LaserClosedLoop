# -*- coding: utf-8 -*-


from guizero import App,Text,TextBox, PushButton
#-----------------------------------------------------------------------------
#Constant values
MIN_VALUE_INTENSITY=0
MAX_VALUE_INTENSITY=10000

#-----------------------------------------------------------------------------
#Function that stores the required intensity
def desired_output():
    if correct_entry_type(desiredIntensity.value)==True:
        if correct_entry_range(float(desiredIntensity.value))==True:
            outputValue.value=desiredIntensity.value
        else:
            outputValue.value= "Please enter a value in the range"
    else:
        outputValue.value= "Please enter a correct value"

#Function that checks if the values is an float
def correct_entry_type(float_output):
    try:
        outputVal = float(float_output)
        return True
    except ValueError:
        print("Please enter a correct value")
        return False

#Function that checks if the values is in a correct range
def correct_entry_range(float_output):
    if (float_output >= MIN_VALUE_INTENSITY) and (float_output <= MAX_VALUE_INTENSITY):
        return True
    else:
        print("Please enter a correct value")
        return False

#-----------------------------------------------------------------------------

#App Display
app= App(title="Closed Loop Laser Intensity Regulator")
welcomeMessage = Text(app,text="Welcome to the Closed Loop Laser intensity regulator software",
                      size=30,color='black')
boxMessage=Text(app,text="Enter the disired laser output intensity")
#Textbox where the user enters the desired intensity
desiredIntensity=TextBox(app,width=50,height=10)
#Button that validates the entry and stores the textbox value as desired output
validationIntensity=PushButton(app,command=desired_output,text="Validate entry")
#Display the value entered (just a sanity check)
outputValue=Text(app, text="The value will appear here")
app.display()
