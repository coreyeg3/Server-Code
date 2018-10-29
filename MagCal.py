
import sys
sys.path.append('./Modules')
import datetime
import smbus
import time
from I2C_SW_CLS import *
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math

XY_Gain = float(450)
Z_Gain = float(400)

print 'Channel to calibrate: '
channel = input()
cal = open("cal.txt"   ,"ax+")

averagingtime = 0.5 ## In minutes
t = time.time()
t_end = t + 60 * averagingtime

while time.time() < t_end:
        try:
            SW.chn(channel)
            lsm303 = Adafruit_LSM303.LSM303()
	    accel, mag = lsm303.read()
	    mag_x, mag_y, mag_z = mag
	    x = float((mag_x/XY_Gain)+0.4255)
	    y = float((mag_y/XY_Gain)-0.657)
	    z = float((mag_z/Z_Gain)-0.4715)
	    f = math.sqrt((x*x) +(y*y) + (z*z))
	    field = round(f,3)
            cal.write("%s,%s,%s,%s,%s\n " % (channel,datetime.datetime.now(),x,y,z))
            time.sleep(0.5)
        except IOError:
            print 'fail'
            pass
        
execfile('avgcal.py')



