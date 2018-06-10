import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

def generateSound(num, time, fs):
    n = time*fs
    x = np.linspace(0, time, n)
    if num == '0':
        freq1 = 1336
        freq2 = 941
    elif num == '1':
        freq1 = 1209
        freq2 = 697
    elif num == '2':
        freq1 = 1336
        freq2 = 697
    elif num == '3':
        freq1 = 1477
        freq2 = 697
    elif num == '4':
        freq1 = 1209
        freq2 = 770
    elif num == '5':
        freq1 = 1336
        freq2 = 770
    elif num == '6':
        freq1 = 1477
        freq2 = 770
    elif num == '7':
        freq1 = 1209
        freq2 = 852
    elif num == '8':
        freq1 = 1336
        freq2 = 852
    elif num == '9':
        freq1 = 1477
        freq2 = 852
    else:
        freq1 = 0
        freq2 = 0

    s1 = (np.sin(freq1*x*2*np.pi))
    s2 = (np.sin(freq2*x*2*np.pi))
    s = s1 + s2

    sd.play(s, 44100)
    sd.wait()

    # Plotting graphs
    plt.figure(1)
    plt.subplot(211)
    plt.plot(s1)
    plt.xlim(0, 250)
    
    plt.subplot(211)
    plt.plot(s2)
    plt.xlim(0, 250)

    plt.subplot(212)
    plt.plot(s)
    plt.xlim(0, 250)
    
    plt.show()
    return


while(True):
    print("Enter a number:")
    num = input()

    generateSound(num, 1, 44100)
    continue