'''
Sampling Frequency of ~330 Hz
'''
import csv
import mmap
import os
import numpy as np

## 'test.txt' is a placeholder file for data in time intervals
try:
	os.remove("test.txt")
except OSError: 
	pass
## Variable initialization
ti = []
f0 = []
f1 = []
f2 = []
f5 = []
f6 = []
f7 = []
######################################################################
## Deleting the last line of data since data may have been interrupted 
lines = file('cal.txt', 'r').readlines() 
# del lines[-1]
file('test.txt','wx+').writelines(lines)
######################################################################
os.remove("cal.txt")
## fill the variables to average
with open("test.txt","r") as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:      
        channel.append(float(row[0]))
        time.append(float(row[1]))
        x.append(float(row[2]))
        y.append(float(row[3]))
        z.append(float(row[4]))
N=len(ti)



channel = '%05.3f' % np.average(channel)
avgx = '%05.3f' % np.average(x)
avgy = '%05.3f' % np.average(y)
avgz = '%05.3f' % np.average(z)
os.remove("test.txt")
with open("calibration_%s.txt"% channel, "a+") as f:
    f.write("%s," % channel)
    f.write("%s," % avgx)
    f.write("%s," % avgy)
    f.write("%s," % avgz)

