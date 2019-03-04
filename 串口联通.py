# -*- coding: utf-8 -*-
"""


@author: linlab
"""
import serial
serialport1 = serial.Serial("com6",115200,timeout=1)
A='55013233AA'
writeData = bytes.fromhex(A) 
#serialport1.write(writeData)

serialport1.write(writeData)
b=serialport1.read().hex()
print( b[::4])
