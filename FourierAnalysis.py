# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy.signal import find_peaks_cwt

def FourierAnalysis(y,Fs,N=1):

    L = len(y)    
    f = (Fs/L)*np.linspace(0.0,(L/2.0),(L/2.0)+1) #Frequency vector       

    #Fft-calculation:
    yf = np.fft.fft(y)
    P2 = np.abs(yf)/L
    P1 = P2[0:(L/2.0)+1]
    P1[1:-2] = 2*P1[1:-2]

    #Calculating the peaks using scipy.signal
    peaks = find_peaks_cwt(P1,np.diff(f)/10.0)
    peaks = np.asarray(peaks)
    yList = np.asarray([P1[peaks],f[peaks],peaks],).transpose()

    data = pd.DataFrame(yList,columns=['Amp', 'Freq','Peak'])
    data = data.sort_values('Amp',axis=0,ascending=0)
    data.index = range(len(data.index))
    
    return P1,f,data[0:N]