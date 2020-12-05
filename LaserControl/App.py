# -*- coding: utf-8 -*-


from guizero import App,Text,TextBox, PushButton

#-----------------------------------------------------------------------------
#Function that stores the required intensity
def desiredOutput():
    outputValue.value=desiredIntensity.value;
#-----------------------------------------------------------------------------

app= App(title="Closed Loop Laser Intensity Regulator")

welcomeMessage = Text(app,text="Welcome to the Closed Loop Laser intensity regulator software",
                      size=30,color='black')

boxMessage=Text(app,text="Enter the disired laser output intensity")

desiredIntensity=TextBox(app,width=50,height=10)

validationIntensity=PushButton(app,command=desiredOutput,text="Validate entry")

outputValue=Text(app, text="The value will appear here")

app.display()
