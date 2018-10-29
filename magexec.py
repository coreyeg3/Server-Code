"""
 This code will collect data from Adafruit LSM303DLHC Magnetometers connected to a RPi via Adafruit TCA9548A multiplexer.
 Data will be collected for each channel listed and written to a txt file in 1 second intervals.
 Seperate file for averaging data will be run for selected intervals. 
 Author Corey Gilbert
 Last Updated Oct 16, 2018
"""
import sys
sys.path.append('./Modules')
import smbus
import time
from I2C_SW_CLS import *
import RPi.GPIO as GPIO
import Adafruit_LSM303
import math
import os
import datetime
#sys.path('/home/pi/mag/Servercode/ServerCode/Modules')

## Gain settings for magnetometer +/- 1.9 Gauss
XY_Gain = float(450)
Z_Gain = float(400)

averagingtime = 1 #Minutes

while True:
	t = time.time()
	t_end = t + 60 * averagingtime
	try:
		os.remove("data.txt")
	except OSError:
		pass
	data = open("data.txt","ax+") ## file to be opened for averaging
	log = open("./logfiles/log.txt","a+")
	while time.time() < t_end:
		data.write("%s," % time.time())
		## Channel 0 ##
		try:
			channel = 0
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			# Difference from probe
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field0 = round(f,4)
			if(field0>8.100):
				data.write("0.000,")
				log.write("%s Sensor 0 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field0)
				pass
		except IOError:
			data.write("0.000,")
			log.write("%s Sensor 0 fail\n" % datetime.datetime.now())
			pass

	## Channel 1 ##
		try:
			channel = 1
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field1 = round(f,4)
			if(field1>8.100):
				data.write("0.000,")
				log.write("%s Sensor 1 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field1)
				pass
		except IOError:
			data.write("0.000,")
			log.write("%s Sensor 1 fail\n" % datetime.datetime.now())
			pass

	## Channel 2 ##
		try:
			channel = 2
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field2 = round(f,3)
			if(field2>8.100):
				data.write("0.000,")
				log.write("%s Sensor 2 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field2)
				pass
		except IOError:
			data.write("0.000,")
			log.write("%s Sensor 2 fail\n" % datetime.datetime.now())
			pass

	## Channel 5 ##
		try:
			channel = 5
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field5 = round(f,3)
			if(field5>8.100):
				data.write("0.000,")
				log.write("%s Sensor 5 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field5)
				pass
		except IOError:
			data.write("0.000,")
			log.write("%s Sensor 5 fail\n" % datetime.datetime.now())
			pass

	## Channel 6 ##
		try:
			channel = 6
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field6 = round(f,3)
			if(field6>8.100):
				data.write("0.000,")
				log.write("%s Sensor 6 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field6)
				pass
		except IOError:
			data.write("0.000,")
			log.write("%s Sensor 6 fail\n" % datetime.datetime.now())
			pass

	## Channel 7 ##
		try:
			channel = 7
                        SW.chn(channel)
                        lsm303 = Adafruit_LSM303.LSM303()
                        time.sleep(0.01)
			accel, mag = lsm303.read()
			mag_x, mag_y, mag_z = mag
			X_Cal = 0
			Y_Cal = 0
			Z_Cal = 0

			x = float((mag_x/XY_Gain)+X_Cal)
			y = float((mag_y/XY_Gain)+Y_Cal)
			z = float((mag_z/Z_Gain)+Z_Cal)
			f = math.sqrt((x*x) +(y*y) + (z*z))
			field7 = round(f,3)
			if(field7>8.100):
				data.write("0.000,")
				log.write("%s Sensor 7 too high\n" % datetime.datetime.now())
			else:	
				data.write("%s," % field7)
				pass
		except IOError:
			data.write("0.000 \n")
			log.write("%s Sensor 7 fail\n" % datetime.datetime.now())
			pass
		
		time.sleep(0.25) ## Sample frequency
	log.write('')
	log.close()
	data.close()	
	execfile('avg.py')

	






