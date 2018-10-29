import smbus
import time
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math
import datetime
import sys
sys.path.append('./Modules')
from I2C_SW_CLS import *

XY_Gain = float(450)
Z_Gain = float(400)


MagMinX = 0
MagMaxX = 0
MagMinY = 0
MagMaxY = 0
MagMinZ = 0
MagMaxZ = 0

print '--------------------------------------------------------'
print 'Starting up calibration program for LSM303 Magnetometers'
print 'Rotate each sensor slowly in all directions until '
print 'each number stops updating. when finished press ctrl + c'
print '--------------------------------------------------------'
print 'Channel to calibrate: '
channel = input()
f=open("axisshift_%s" % channel,'ax+')
while True: 
        try:           
            SW.chn(channel)
            lsm303 = Adafruit_LSM303.LSM303()
	    accel, mag = lsm303.read()
	    mag_x, mag_y, mag_z = mag
	    x = round(float((mag_x/XY_Gain)),3)
	    y = round(float((mag_y/XY_Gain)),3)
	    z = round(float((mag_z/Z_Gain)+0.8),3)
            if (x < MagMinX):
                MagMinX = round(x,3)
                pass
            if (x > MagMaxX):
                MagMaxX = round(x,3)
                pass
            if (y < MagMinY):
                MagMinY = round(y,3)
                pass
            if (y > MagMaxY):
                MagMaxY = round(y,3)
                pass
            if (z < MagMinZ):
                MagMinZ = round(z,3)
                pass
            if (z > MagMaxZ):
                MagMaxZ = round(z,3)
                pass
            print '%s %s %s %s %s %s' %( MagMinX, MagMaxX, MagMinY, MagMaxY, MagMinZ, MagMaxZ)
            time.sleep(0.1)
        except IOError:
                print 'Fail'
                pass
        except KeyboardInterrupt:         
                x_shift = (MagMinX + MagMaxX)/2
                y_shift = (MagMinY + MagMaxY)/2
                z_shift = (MagMinZ + MagMaxZ)/2
                f.write('%s\n' % x_shift)
                f.write('%s\n' % y_shift)
                f.write('%s\n' % z_shift)
                f.close()
                break


