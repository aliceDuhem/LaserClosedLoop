# New version of the application gathering the user inputs
# Use a more intuitive GUI with abstracted threading
# Last updated: 01/06/21

import tkinter as tk
import tkinter.messagebox
import threading
from threading import Thread
from time import sleep
#Reads the Power from the power meter
from GetPower import PowerMeter
#Computed the angles
from RatioFinal import difference
from RatioFinal import absolute
from RatioFinal import ratio
#Calibrates the motor
from MotorCalibration import Calibration
#Connection with the Raspberry Pi
from ConnectionR import Connect
#-------------------------------------------------------------------------------
#Define all the constants
MIN_VALUE_POWER=0
MAX_VALUE_POWER=1000
MIN_TRANSMITTANCE=0
MAX_TRANSMITTANCE=1
MIN_INCREMENT=0.0001
MAX_INCREMENT=4
#-------------------------------------------------------------------------------

# Main GUI

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #Gives a name to the window
        master.title('Laser Intensity Regulator Application')
        # Width height of the window
        master.geometry("500x500")
        # Create widgets/grid, where the components are going to be put
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        #Determines if the thread is active or not (hence if the code if fetching laser intnesity or not)
        self.thread_status = True
        #Are the elements in the entries correct?
        self.no_error = False

        #Main Values for the experiement
        self.outputValue=0
        self.motorIncrement=0.18
        self.HWPTransmittance=0.9
        self.cubeTransmittance=0.9
        self.cubeRefTransmittance=0.95
        self.currentMotorAngle=0

        #TODO: Create a connection with the RPi or arduino



#Determines the layout of the app
    def create_widgets(self):

        # Laser power
        self.laser_power_text = tk.StringVar()
        #Write the label for the laser power.
        #pady 20 puts some space between the top of the page and the text
        self.laser_power_label = tk.Label(
            self.master, text='Desired Laser output power', font=('bold', 14), pady=20, padx=10)
        self.laser_power_label.grid(row=0, column=0)
        #Put the entry after the text
        self.laser_power_entry = tk.Entry(self.master, textvariable=self.laser_power_text, justify='center')
        self.laser_power_entry.grid(row=1, column=0)

        # Motor increment
        self.motor_inc_text = tk.StringVar()
        self.motor_inc_text.set("0.2")
        self.motor_inc_label = tk.Label(
            self.master, text='Motor Increment', font=('bold', 14), pady=20, padx=10,anchor="center")
        self.motor_inc_label.config(anchor= "e")
        self.motor_inc_label.grid(row=3, column=0)
        self.motor_inc_entry = tk.Entry(
            self.master, textvariable=self.motor_inc_text, justify='center')
        self.motor_inc_entry.grid(row=4, column=0)

        # Half wave plate transmittance
        self.hwpt_text = tk.StringVar()
        self.hwpt_text.set("0.9")
        self.hwpt_label = tk.Label(
            self.master, text='Half Wave plate Transmittance', pady=20, padx=10, font=('bold', 14))
        self.hwpt_label.grid(row=5, column=0)
        self.hwpt_entry = tk.Entry(
            self.master, textvariable=self.hwpt_text, justify='center')
        self.hwpt_entry.grid(row=6, column=0)

        # Cube Transmittance
        self.cubet_text = tk.StringVar()
        self.cubet_text.set("0.9")
        self.cubet_label = tk.Label(
            self.master, text='Cube Transmittance', pady=20, padx=10, font=('bold', 14))
        self.cubet_label.grid(row=7, column=0)
        self.cubet_entry = tk.Entry(
            self.master, textvariable=self.cubet_text, justify='center')
        self.cubet_entry.grid(row=8, column=0)

        # Cube Ref Transmittance
        self.cubert_text = tk.StringVar()
        self.cubert_text.set("0.95")
        self.cubert_label = tk.Label(
            self.master, text='Cube Reflection Transmittance', pady=20, padx=10, font=('bold', 14))
        self.cubert_label.grid(row=9, column=0)
        self.cubert_entry = tk.Entry(
            self.master, textvariable=self.cubert_text, justify='center')
        self.cubert_entry.grid(row=10, column=0)

        #(Re-)Validation Button
        self.validation_button=tk.Button(self.master, text="Initialise", command=self.initialise_motor,font=('bold', 14), pady=10, height=1, width=15)
        self.validation_button.grid(row=2, column=1, rowspan=2)

        #Start Button
        #Start the thread which starts the control code
        self.start_button=tk.Button(self.master, text="Start",command=self.start_thread, font=('bold', 14), pady=10, height=1, width=15)
        self.start_button.grid(row=4, column=1, rowspan=2)

        #Stop Button
        self.stop_button=tk.Button(self.master, text="Stop",command=self.stop_thread,font=('bold', 14), pady=10, height=1, width=15)
        self.stop_button.grid(row=6, column=1, rowspan=2)


    #Add the definitions of the functions
    def initialise_motor(self):
        cal=Calibration()
        print("initialise_motor() called")

        #Code to initialise the motor
        #1. create a power meter instance
        pm = PowerMeter()

        #Set the motor to 0
        cal.motor_to_0(pm)
        self.currentMotorAngle=0

        #Set the motor to the wanted Power
        #self.currentMotorAngle=Calibration.motor_to_initial_power(pm,self.outputValue,self.motorIncrement,self.cubeTransmittance,self.cubeRefTransmittance,self.HWPTransmittance)


    def start_thread(self):
        print('start_thread() called')
        self.validation()
        self.thread_status=True
        if (self.no_error):
            Thread(target=self.activate_system).start()


    def activate_system(self):
        #Add the control loop of the system and send the info to a RPi
        print('activate_system called')
        print(self.thread_status)
        data_array=[]

        while self.thread_status:
            print("active")
            sleep(1)
            #code


        #1. Create the power meter and get the power
            pm = PowerMeter()

        #2. Do the computation using the class
            instPower=pm.readPower(pm.power_meter)
            angleComputed = difference.neededAngle(self.currentMotorAngle, instPower,self.motorIncrement,self.outputValue,self.cubeTransmittance,self.cubeRefTransmittance,self.HWPTransmittance)
            angleRotation = self.currentMotorAngle-angleComputed
            steps= angleRotation/self.motorIncrement
            self.currentMotorAngle=self.currentMotorAngle+angleRotation
            a=[datetime.datetime.now(),instPower,angleComputed]
            data_array.append(a)

        #3. Send to the RPi the information using the connection class
            rpi=Connect()
            """rpi.sendPacket(steps)"""

    #Write the values in CSV file for data analysis
        createCsvFileData(data_array)
        del data_array

    def stop_thread(self):
        #Stop the operation of the control loop
        self.thread_status=False
        print("Process stopped")

#IGNORE CODE BELOW, DATA ANALYSIS AND CHECKING
#*******************************************************************************
#*******************************************************************************
    #Check data Entry
    #-----------------------------------------------------------------------------
    def validation(self):
        if self.correct_entry_type(self.laser_power_text.get())==True:  #self.laser_power_text.get(): to get the value inside the textbox, .get() function required
            if self.correct_entry_range_power(self.laser_power_text.get())==True:
                self.outputValue=float(self.laser_power_text.get())
            else:
                print("Please enter a number for Laser power")
                tkinter.messagebox.showwarning(title="Laser Power Error", message="Please enter a correct Laser power in the range 0-10000")
                self.no_error = False
        else:
            print("Please enter a number for Laser power")
            tkinter.messagebox.showwarning(title="Laser Power Error", message="Please enter a number for Laser power")
            self.no_error = False

        if self.correct_entry_type(self.motor_inc_text.get())==True:
            if self.correct_entry_range_increment(self.motor_inc_text.get())==True:
                self.motorIncrement=float(self.motor_inc_text.get())
            else:
                tkinter.messagebox.showwarning(title="Motor Increment Error", message="Please enter a Motor Increment in the range 0.0001-4")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Motor Increment Error", message="Please enter a Motor Increment")
            self.no_error = False

        if self.correct_entry_type(self.hwpt_text.get())==True:
            if self.correct_entry_range_transmittance(self.hwpt_text.get())==True:
                self.HWPTransmittance=float(self.hwpt_text.get())
            else:
                tkinter.messagebox.showwarning(title="Half Wave Plate Transmittance", message="Please enter a Half Wave Plate Transmittance in the range 0-1")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Half Wave Plate Transmittance", message="Please enter a correct Half Wave Plate Transmittance")
            self.no_error = False

        if self.correct_entry_type(self.cubet_text.get())==True:
            if self.correct_entry_range_transmittance(self.cubet_text.get())==True:
                self.cubeTransmittance=float(self.cubet_text.get())
            else:
                tkinter.messagebox.showwarning(title="Cube Transmittance", message="Please enter a Cube Transmittance in the range 0-1")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Cube Transmittance", message="Please enter a correct Cube Transmittance")
            self.no_error = False

        if self.correct_entry_type(self.cubert_text.get())==True:
            if self.correct_entry_range_transmittance(self.cubert_text.get())==True:
                self.cubeRefTransmittance=float(self.cubert_text.get())
            else:
                tkinter.messagebox.showwarning(title="Reflected Cube Transmittance", message="Please enter a Reflected Cube Transmittance in the range 0-1")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Reflected Cube Transmittance", message="Please enter a correct Reflected Cube Transmittance")
            self.no_error = False

        if (self.correct_entry_type(self.laser_power_text.get())==True & self.correct_entry_range_power(self.laser_power_text.get())==True)&(self.correct_entry_type(self.motor_inc_text.get())==True&self.correct_entry_range_increment(self.motor_inc_text.get())==True)&(self.correct_entry_type(self.hwpt_text.get())==True & self.correct_entry_range_transmittance(self.hwpt_text.get())==True)&(self.correct_entry_type(self.cubet_text.get())==True & self.correct_entry_range_transmittance(self.cubet_text.get())==True):
            textval = 'Entry validation:\nDesired Output = '+str(self.outputValue)+'W\n Motor Increment = '+str(self.motorIncrement)+'\nHalf Wave Plate Transmittance='+str(self.HWPTransmittance)+'\nCube Transmittance ='+str(self.cubeTransmittance)
            print(textval)
            self.no_error = True

    #Function that checks if the values is an float
    def correct_entry_type(self,float_output):
        try:
            outputVal = float(float_output)
            return True
        except ValueError:
            print("Please enter a number")
            return False

    #Function that checks if the values is in a correct range
    def correct_entry_range_power(self,float_output):
        if (float(float_output) >= MIN_VALUE_POWER) and (float(float_output) <= MAX_VALUE_POWER):
            return True
        else:
            print("Please enter a value in the range 0-10000")
            return False

    def correct_entry_range_increment(self,float_output):
        if (float(float_output) >= MIN_INCREMENT) and (float(float_output) <= MAX_INCREMENT):
            return True
        else:
            print("Please enter a value in the range 0.001-2")
            return False

    def correct_entry_range_transmittance(self,float_output):
        if (float(float_output) >= MIN_TRANSMITTANCE) and (float(float_output) <= MAX_TRANSMITTANCE):
            return True
        else:
            print("Please enter a value in the range 0-1")
            return False
    #---------------------------------------------------------------------------

    #Create a class to write in the csv file all the data
    #The columns will give the intensity and the error
    def createCsvFileData(data):


        docName = 'power_readings_' #beginning name document
        date_time = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S")   #adds the time to the title to make it unique
        file_extension =  '.csv'    #needs the file extension in the name
        alreadyExists_str = 'second_'
        fileName = docName+str(wantedPower)+'W_motorInc'+str(motorIncrement)+'_'+date_time+file_extension
        columns = ['timestamp','power','error'] #determines the 3 columns of the file
        separator = ',' #separator between the 3 columns in a row
        format_columns = ['%s','%.6f','%.6f']   #the datatype of the columns

        #makes sure that the headings and the columns are of the same dimensions
        if len(data[0]) != len(columns):
            print ("The dimensions of the columns and headings are not equal")
            return

        #check if the file exists if needed in order not to overwrite
        if(os.path.exists(fileName)):
            print("The file already exists")
            fileName=docName+alreadyExists_str+date_time+file_extension

        #Specifies the path mode as writing 'w'
        file = open(fileName, 'w')

        #Writes an header/description of the document: time the measures started
        line = 'Intensity recordings for experiment starting at '+ str(data[0][0]) +'. readings every '+ str(data[1][0]-data[0][0]) + ' seconds\n'
        file.write(line)

        #each case of columns is separates on a line by a comma (separator),
        #concatenated and added to the file
        #line is a template for the format
        line = separator.join(columns)
        file.write('%s\n' % line)

        #for each new row in the data, give the correct type format
        format = separator.join(format_columns)
        for row in data:
            line= format % tuple(row)
            file.write('%s\n' % line)

        #close the file
        file.close()

    def formatDateTime(date_time):
        date_time = date_time.strftime("%Y-%b-%d %H:%M:%S") #gives the correct format to the time
#*******************************************************************************
#*******************************************************************************


root = tk.Tk()
app = Application(master=root)
app.mainloop()
