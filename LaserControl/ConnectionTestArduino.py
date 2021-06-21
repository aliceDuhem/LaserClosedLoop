# Written using https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
import serial
import time

#You might need to change the port number
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)

def send(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    #arduino.write(bytes('0', 'utf-8'))
    #data = arduino.readline()
    return data

"""Code ARDUINO:

// Pin connections
const int dirPin = 2;
const int stepPin = 3;

void setup()
{
  // Declare pins as Outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  //Used for downstepping
  digitalWrite(4, HIGH);

   Serial.begin(9600);
   Serial.setTimeout(1);
}
void loop()
{

  while (!Serial.available());
  step = Serial.readString().toInt();

  for(int x = 0; x <= step ; x++)
  {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(1000);
  }
  delay(100); // Wait 0.1 second
}
"""
