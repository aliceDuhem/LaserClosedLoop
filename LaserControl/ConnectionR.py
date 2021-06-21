import socket
import os

#EXAMPLE of connection to the Raspberry PI

class Connect:

    def __init__(self):
        #Use a UDP portocol to transfer information from the RaspberryPi to the
        #The computer is the client sending data to the server (RPi)
        self.UDP_PORT_RPi = 5021

        #Need to find the IP of your RPi
        self.UDP_IP_RPi = "192.168.43.123"

        #create a socket between internet and UDP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.UDP_IP_RPi, self.UDP_PORT_RPi))


    #Sends angle to rotate to the RaspberryPi
    def sendPacket(self, data):
        angle = bytes(str(data),'utf-8')
        print(angle)
        self.sock.sendto(angle, (self.UDP_IP_RPi, self.UDP_PORT_RPi))
        print("sent")

data = 8
connect = Connect()
connect.sendPacket(data)


"""For the RPi (server)
import socket
import os

#Listens to any source
UDP_IP = "0.0.0.0"
UDP_PORT = 12345
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
#It is a float number 8bits (take 16 as buffer to be sure)
  data, addr = sock.recvfrom(16)
  print("received message:", data)

 #Code to rotate the device

  if data==1'LED=1\n':
    print("This works")
    elif data==2'LED=0\n':
    print("youhou")


"""
