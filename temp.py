import numpy as np
import matplotlib.pyplot as plt
import serial
import sys, argparse
import matplotlib.animation as animation
from drawnow import drawnow

strPort1 = '/dev/cu.usbmodem1411' # define the port that connects arduino to computer.
strPort2 = '/dev/cu.usbmodem1421'
plt.ion() # turns the interactive mode on and allows one to plot live data

x=list()
y=list()
i=0


ser = serial.Serial(strPort2, 9600) # Connects arduino port to python
ser.close() 
ser.open() 

def makefig1(): # we can change the plot number by changing the first value in the suplot function
    fig1,axes = plt.subplots(16, 1,figsize = (20, 28),sharex = True) 
    for i, ax in enumerate(axes): # loop through each element in axes while keeping track of iteration through enumerate
        ax.plot(v_plot[i], 'o')
    fig1.suptitle('Temperature Monitor', size=(15))

v_plot = [list() for _ in range(16)] 

while True:  
    while (ser.inWaiting()==0): # waits for data to come in from the port
        pass 

    data = ser.readline() 
    raw_data = data.decode()  # The decode function decodes the values coming from the arduino into readable data
    raw = raw_data.strip() # I stripped any unwanted strings from the list
    v_read = raw.split()    #split the value at each seperator, in this case the spaces between each value
    for _, v in enumerate(v_read):    #loop through the split data
        v_plot[_].append(float(v))     # appends data value to the variable v_plot

    print(v_plot)
    drawnow(makefig1) # plots the updated figure
    x.append(i)
    i += 1
    plt.pause(3) #pauses the plot at given value(in seconds)
    plt.savefig('makefig1.png')
