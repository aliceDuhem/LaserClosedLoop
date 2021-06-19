import pyfirmata
from pyfirmata import Arduino,servo
import time

board = pyfirmata.Arduino('COM5')

while True:
    board.digital[13].write(1)
    time.sleep(0.25)
    board.digital[13].write(0)
    time.sleep(0.5)

#Angle in number of steps

q
