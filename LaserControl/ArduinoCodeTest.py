import serial

#Open the port with no timeout
ser = serial.Serial('COM5',9600)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port

def run(self):
    run_char= "r"
    data[0] = run_char.encode()
    print (data)
    ser.write(data)
    print ("run")

def send_stop(self):
    stop = "s"
    self.data[0] =stop.encode()
    data[0] = run_char.encode()
    print (data)
    ser.close()
    ser = serial.Serial('COM5',9600)
    time.sleep(0.05)
