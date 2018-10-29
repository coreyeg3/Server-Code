'''
The purpose of this code is to listen for a request fron the PROSPECT Slow Controls system 
and send averaged data from magnetometers
Author: Corey Gilbert
cgilbe15@vols.utk.edu
Copyright 2018
Last revised: 6 Sept 2018
'''

import socket
import sys
import mmap
import time
import os

def touch(fname, times=None):
	with open(fname, 'a+'):
		os.utime(fname, times)
touch('./logfiles/socketlog.txt')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('0.0.0.0', 5000)
sock.bind(server_address)

sock.listen(1)


while 1:
        
        connection, client_address = sock.accept()
	touch('./logfiles/socketlog.txt')
        if connection:
            with open('memmap.txt','r+') as a:
                    mm = mmap.mmap(a.fileno(),0)
                    field0 = mm[:5]
                    field1 = mm[6:11]
                    field2 = mm[12:17]
                    field5 = mm[18:23]
                    field6 = mm[24:29]
                    field7 = mm[30:35]
                    avgt = mm[36:]

                    field0 = field0 + '\n'
                    field1 = field1 + '\n'
                    field2 = field2 + '\n'
                    field5 = field5 + '\n'
                    field6 = field6 + '\n'
                    field7 = field7 + '\n'

            while True:
                    data = connection.recv(16)
                    f = open('socketlog.txt','a+')
                    if not data:
                        f.write('%s ' % time.time())
                        f.write('no data\n')
                        break
                    if 'field0' in data:
                            connection.send(field0)
                            f.write('%s ' % time.time())
                            f.write('f0 sent\n')
                            f.close()
                    elif 'field1' in data:
                            connection.send(field1)
                            f.write('%s ' % time.time())
                            f.write('f1 sent\n')
                            f.close()
                    elif 'field2' in data:
                            connection.send(field2)
                            f.write('%s ' % time.time())
                            f.write('f2 sent\n')
                            f.close()
                    elif 'field5' in data:
                            connection.send(field5)
                            f.write('%s ' % time.time())
                            f.write('f5 sent\n')
                            f.close()
                    elif 'field6' in data:
                            connection.send(field6)
                            f.write('%s ' % time.time())
                            f.write('f6 sent\n')
                            f.close()
                    elif 'field7' in data:
                            connection.send(field7)
                            f.write('%s ' % time.time())
                            f.write('f7 sent\n')
                            f.close()
                    else:
                            f.write('%s' % time.time())
                            f.write('error in request\n')
                            connection.send("error invalid selection\n")
                            f.close()
        else:
            f = open('socketlog.txt','a+')
            f.write('closed\n')
            connection.close()
            pass           
        time.sleep(10)
