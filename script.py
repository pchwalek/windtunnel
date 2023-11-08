from playsound import playsound

import serial 
import time

# s = serial.Serial('COM5')
s = serial.Serial('/dev/cu.usbmodem91431001')

s.write(1)

#playsound("basic-sine-riser-71661.mp3")
#on mac, I did 5 clicks down from max

playsound("injected_sounds/start.mp3")

wind_speed_values = [1,
515,
840,
1275,
1540,
1890,
2240,
2660]
# 2930,
# 3280,
# 3635,
# 3790,
# 4097]

#operating amperage: 0.033 A
print("first experiment: please have fans unplugged")
print("make sure volume is at 75%")
time.sleep(15)
playsound("injected_sounds/pink-noise.mp3")

s.write(1)

playsound("injected_sounds/complete.mp3")
print("PLUG IN FANS")
time.sleep(30)

print(" waiting for 90s")
time.sleep(90)
print(" playing bee sound")
playsound("bee-flying-loop-42287.mp3")
print(" playing sine sweep")
playsound("basic-sine-riser-71661.mp3")
s.write(0)
time.sleep(10)
print("PLUG IN FAN POWER")
time.sleep(30)

RAMP_UP_TIME = 60
TEST_TIME = 30

# RAMP_UP_TIME = 20
# TEST_TIME = 10

for i in range(len(wind_speed_values)):
    print("test number: " + str(i))
    s.write((str(wind_speed_values[i]) + '\r').encode())
    s.write('\r'.encode());
    print(" waiting for 60s rampup")
    time.sleep(RAMP_UP_TIME)
    print(" 30s capture")
    time.sleep(TEST_TIME)
    print(" playing bee sound")
    playsound("injected_sounds/bee-flying-loop-42287.mp3")
    print(" playing sine sweep")
    playsound("injected_sounds/basic-sine-riser-71661.mp3")
    # s.write(0)
    time.sleep(10)

print("TEST DONE")
playsound("injected_sounds/complete.wav")
playsound("injected_sounds/complete.wav")
s.write(1)
