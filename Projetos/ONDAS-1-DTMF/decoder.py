from mySignal import mySignal
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks_cwt
import peakutils
import time


funcs = mySignal()

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1
duration = 4


def recordSound():
    print("Recording for", duration ,"sec...")
    myrecording = sd.rec(int(duration * fs)) 
    sd.wait()
    myrecording = myrecording[:,0]
    return myrecording

def calcPeaks(signal):
    x, y = funcs.calcFFT(signal)
    indexes = peakutils.indexes(y, thres=0.5, min_dist=40)
    for i in range(len(indexes)):
        indexes[i] = indexes[i]/duration
    return indexes

def analyseFreqs(freqs):
    if 690 <= freqs[0] <= 704:
        if 1202 <= freqs[1] <= 1216:
            return 1
        elif 1329 <= freqs[1] <= 1343:
            return 2
        elif 1470 <= freqs[1] <= 1484:
            return 3
        else:
            return -1
    
    elif 763 <= freqs[0] <= 777:
        if 1202 <= freqs[1] <= 1216:
            return 4
        elif 1329 <= freqs[1] <= 1343:
            return 5
        elif 1470 <= freqs[1] <= 1484:
            return 6
        else:
            return -1
    
    elif 845 <= freqs[0] <= 859:
        if 1202 <= freqs[1] <= 1216:
            return 7
        elif 1329 <= freqs[1] <= 1343:
            return 8
        elif 1470 <= freqs[1] <= 1484:
            return 9
        else:
            return -1
    else:
        return -1

while (1):
    print("Press enter to start recording:")
    input()

    signal = recordSound()
    maxsignal = np.max(abs(signal))
    signal = signal/maxsignal
    
    freqs = calcPeaks(signal)

    tone = analyseFreqs(freqs)

    if tone != -1:
        print("O tom discado foi:", tone)
    print ("______________________________________________")
    time.sleep(2)