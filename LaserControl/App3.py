# New version of the application gathering the user inputs
# Use a more intuitive GUI with abstracted threading
# Last updated: 01/06/21

import tkinter as tk
import tkinter.messagebox
import threading
from threading import Thread
from time import sleep
#from GetPower import PowerMeter

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
        master.geometry("500x400")
        # Create widgets/grid, where the components are going to be put
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        #Determines if the thread is active or not (hence if the code if fetching laser intnesity or not)
        self.thread_status = True
        #Are the elements in the entries correct?
        self.no_error = False

        #Values for the experiement
        self.outputValue=0
        self.motorIncrement=0.2
        self.HWPTransmittance=0.1
        self.cubeTransmittance=0.1



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
        self.hwpt_text.set("0.1")
        self.hwpt_label = tk.Label(
            self.master, text='Half Wave plate Transmittance', pady=20, padx=10, font=('bold', 14))
        self.hwpt_label.grid(row=5, column=0)
        self.hwpt_entry = tk.Entry(
            self.master, textvariable=self.hwpt_text, justify='center')
        self.hwpt_entry.grid(row=6, column=0)

        # Cube Transmittance
        self.cubet_text = tk.StringVar()
        self.cubet_text.set("0.1")
        self.cubet_label = tk.Label(
            self.master, text='Cube Transmittance', pady=20, padx=10, font=('bold', 14))
        self.cubet_label.grid(row=7, column=0)
        self.cubet_entry = tk.Entry(
            self.master, textvariable=self.cubet_text, justify='center')
        self.cubet_entry.grid(row=8, column=0)

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
        print("initialise_motor() called")
        #Add the code to initialise the motor

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

        while self.thread_status:
            print("active\n")
            sleep(1)
            #code


    def stop_thread(self):
        #Stop the operation of the control loop
        self.thread_status=False
        print("Process stopped")

    #Check data Entry
    #-----------------------------------------------------------------------------
    def validation(self):
        if self.correct_entry_type(self.laser_power_text.get())==True:  #self.laser_power_text.get(): to get the value inside the textbox, .get() function required
            if self.correct_entry_range_power(self.laser_power_text.get())==True:
                outputValue=float(self.laser_power_text.get())
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
                motorIncrement=float(self.motor_inc_text.get())
            else:
                tkinter.messagebox.showwarning(title="Motor Increment Error", message="Please enter a Motor Increment in the range 0.0001-4")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Motor Increment Error", message="Please enter a Motor Increment")
            self.no_error = False

        if self.correct_entry_type(self.hwpt_text.get())==True:
            if self.correct_entry_range_transmittance(self.hwpt_text.get())==True:
                HWPTransmittance=float(self.hwpt_text.get())
            else:
                tkinter.messagebox.showwarning(title="Half Wave Plate Transmittance", message="Please enter a Half Wave Plate Transmittance in the range 0-1")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Half Wave Plate Transmittance", message="Please enter a correct Half Wave Plate Transmittance")
            self.no_error = False

        if self.correct_entry_type(self.cubet_text.get())==True:
            if self.correct_entry_range_transmittance(self.cubet_text.get())==True:
                cubeTransmittance=float(self.cubet_text.get())
            else:
                tkinter.messagebox.showwarning(title="Cube Transmittance", message="Please enter a Cube Transmittance in the range 0-1")
                self.no_error = False
        else:
            tkinter.messagebox.showwarning(title="Cube Transmittance", message="Please enter a correct Cube Transmittance")
            self.no_error = False

        if (self.correct_entry_type(self.laser_power_text.get())==True & self.correct_entry_range_power(self.laser_power_text.get())==True)&(self.correct_entry_type(self.motor_inc_text.get())==True&self.correct_entry_range_increment(self.motor_inc_text.get())==True)&(self.correct_entry_type(self.hwpt_text.get())==True & self.correct_entry_range_transmittance(self.hwpt_text.get())==True)&(self.correct_entry_type(self.cubet_text.get())==True & self.correct_entry_range_transmittance(self.cubet_text.get())==True):
            textval = 'Entry validation:\nDesired Output = '+str(outputValue)+'W\n Motor Increment = '+str(motorIncrement)+'\nHalf Wave Plate Transmittance='+str(HWPTransmittance)+'\nCube Transmittance ='+str(cubeTransmittance)
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




root = tk.Tk()
app = Application(master=root)
app.mainloop()
