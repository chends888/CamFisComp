import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy.fftpack import fft


############################################################
####################      ENCODING      ####################
############################################################




# Low pass filter
# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
nyq_rate = 44100/2
width = 5.0/nyq_rate
ripple_db = 60.0 #dB
N , beta = kaiserord(ripple_db, width)
cutoff_hz = 4000.0
taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))


def calcFFT(signal):
    # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
    N = len(signal)
    # W = window.hamming(N)
    T = 1/44100
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal)
    return(xf, np.abs(yf[0:N//2]))

def plotFFT(signal, title):
    x, y = calcFFT(signal)
    plt.figure()
    plt.plot(x, np.abs(y))
    plt.title(title)
    plt.show(block = False)



def readFile():
    data, samplerate = sf.read("onclassical_demo_demicheli_geminiani_pieces_allegro-in-f-major_small-version.wav")
    data = data [:,0]

    # Normalization
    maxsignal = np.max(abs(data))
    data = data/maxsignal

    # Applying low pass filter
    data = lfilter(taps, 1.0, data)

    # Plot fourier transform
    plotFFT(data, 'Fourier after low pass filter')

    # Modulation (Multiply by carry)
    n = len(data)
    x = np.linspace(0,20, n)
    carry = (np.sin(15000*x*2*np.pi))
    data = data * carry

    # Plot fourier transform
    plotFFT(data, 'Fourier after modulation')

    return data


############################################################
####################      DECODING      ####################
############################################################


# Multiply by carry
data = readFile()
n = len(data)
x = np.linspace(0,20, n)
carry = (np.sin(15000*x*2*np.pi))
data = data * carry


# Appliyng low pass filter
data = lfilter(taps, 1.0, data)

# Plot fourier transform
plotFFT(data, 'Fourier after demodulation')

# Play demodulated wave
sd.play(data, 44100)
sd.wait()