# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 12:19:13 2016

@author: az18159
"""

import numpy as np
import pandas as pd
from FourierAnalysis import FourierAnalysis
import matplotlib.pyplot as plt 
import seaborn as sns

plt.close('all')

#Test af fourier analysis:
Fs = 1000.0                                   #Sampling frequency
T = 1.0/Fs                                    #Sampling period
L = 1000.0                                    #Length of signal
t = np.linspace(0.0,L-1,L)*T                  #Time vector    
y = np.sin(50.0*2.0*np.pi*t)+0.5*np.sin(80.0*2.0*np.pi*t)+0.3*np.sin(120.0*2.0*np.pi*t)

#Finding the amplitude and frequency of the signal
P1,f,data = FourierAnalysis(y,Fs,N=3)
print data

#Plotting the signal
plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.plot(t,y)
plt.title('Signal', fontsize=14)
plt.ylabel('y',fontsize=14)
plt.xlabel('t [s]',fontsize=14)

#Plotting the fft-plot
plt.subplot(2,1,2)
plt.plot(f,P1)
#plt.title('fft-plot', fontsize=14)
plt.ylabel('Amplitude',fontsize=14)
plt.xlabel('Frequency [Hz]',fontsize=14)

for i in data.Freq:
    plt.plot((i,i),(0,1),color='k',linestyle='--')

plt.savefig('FftPlot.jpg')