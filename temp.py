import numpy as np
import matplotlib.pyplot as plt
import serial
import sys, argparse
import matplotlib.animation as animation
from drawnow import drawnow
# web_dir =

# from time import sleep
# from collections import deque

strPort1 = '/dev/cu.usbmodem1411' # define the port that connects arduino to computer.
strPort2 = '/dev/cu.usbmodem1421'
plt.ion() # turns the interactive mode on and allows one to plot live data

x=list()
y=list()
i=0

# to execute code, open terminal and write: python file name
ser = serial.Serial(strPort2, 9600) # Connects arduino port to python
ser.close() # closes the port
ser.open() # re-opens the port

def makefig1(): # Defined a function that has the subplot of different voltage values
    fig1,axes = plt.subplots(16, 1,figsize = (20, 28),sharex = True) # we can change the plot number by changing the first value in the suplot function
    for i, ax in enumerate(axes): # loop through each element in axes while keeping track of iteration through enumerate
        ax.plot(v_plot[i], 'o')
    fig1.suptitle('Temperature Monitor', size=(15))

v_plot = [list() for _ in range(16)] #created an empty list for each value we shall plot

while True:  # using while loop to keep the plot running
    while (ser.inWaiting()==0): # waits for data to come in from the port
        pass # does nothing

    data = ser.readline() # The serial values from the arduino serial monitor are defined as data
    raw_data = data.decode()  # The decode function decodes the values coming from the arduino into readable data
    raw = raw_data.strip() # I stripped any unwanted strings from the list
    v_read = raw.split()    #split the value at each seperator, in this case the spaces between each value
    for _, v in enumerate(v_read):    #for-loop that loops through the split data
        v_plot[_].append(float(v))     # appends the data value to the variable v_plot

    print(v_plot)
    drawnow(makefig1) # plots the updated figure
    x.append(i)
    i += 1
    plt.pause(3) #pauses the plot at given value(in seconds)
#     for _ in v_plot:
#         if (i>50):
#             v_plot[_].pop(0)
    plt.savefig('makefig1.png')
