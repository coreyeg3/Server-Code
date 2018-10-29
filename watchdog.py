'''
Watchdog program to check for file modification
Author: Corey Gilbert
Affiliation: Oak Ridge National Lab / University of Tennessee
Copyright 2018
'''
import os
import time
import datetime
while 1:
    f = open('./logfiles/wdg_log.txt', 'a+')
    magexec = './logfiles/log.txt' ## Path of file you want to watch
    socket = './logfiles/socketlog.txt'
    last_update_mag = os.path.getmtime(magexec)
    last_update_socket = os.path.getmtime(socket)
    current_time = time.time()
    timer_duration = 15 ## Seconds
    if (current_time - last_update_mag >= timer_duration):
        f.write( '%s WTH something is not running.\n' % datetime.datetime.now())
        execfile('magexec.py')
        time.sleep(5)
        f.close()
    if (current_time - last_update_mag <= timer_duration):
        time.sleep(5)
        pass
    if (current_time - last_update_socket >= timer_duration):
        f.write( '%s WTH something is not running.\n' % datetime.datetime.now())
        execfile('listen.py')
        time.sleep(5)
        f.close()
    if (current_time - last_update_socket <= timer_duration):
        time.sleep(5)
        pass