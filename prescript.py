from playsound import playsound

import serial 
import time

s = serial.Serial('COM5')
#s = serial.Serial('/dev/cu.usbmodem91431001')


print("starting test. make sure fans are unpowered")
time.sleep(60)
playsound("bee-flying-loop-42287.mp3")
playsound("basic-sine-riser-71661.mp3")






