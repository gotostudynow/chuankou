# -*- coding: utf-8 -*-
import serial

import math
import matplotlib.pyplot as plt

serialport1 = serial.Serial("com6",115200,timeout=1)
A='55013233AA'
n=0
X=[]
Y=[]# 开启一个画图的窗口
plt.ion()

while(n<1250):
    writeData = bytes.fromhex(A) 
    #serialport1.write(writeData)
    serialport1.write(writeData)
    b=serialport1.read().hex()
    n+=1
    print(b)
    if((n%11)==4):
        x1=b
    if((n%11==5)):
        x2=bin(int((x1+b),16))
        x2=str(x2)
        x2=list(x2)
        print(type(x2))
        
        if(((x2)[2])==0):
             x2=x2
        else:
             x2=x2[3:]
             x2="".join(x2)
             print(type(x2))
             print(x2)
             x2=-int(x2, 2)
        X.append(x2)
    
        print("X=")
        print(X)
    if(n%11==6):
        y1=b
    if(n%11==7):
        y2=bin(int((y1+b),16))
        y2=str(y2)
        y2=list(y2)
        if(((y2)[2])==0):
           y2=y2
        else:
            y2=y2[3:]
            y2="".join(y2)
            y2=-int(y2,2)

        
        Y.append(y2)
        
        print("Y=")
        print(Y)
        plt.clf()
        plt.plot(X)
        plt.show()
        plt.plot(Y)
        plt.show()
        plt.pause(0.1) 
       
