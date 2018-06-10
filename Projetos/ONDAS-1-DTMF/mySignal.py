import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

# sd.default.samplerate = 44100


class mySignal:
    def __init__(self):
        self.init = 0

    def calcFFT(self, signal):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N = len(signal)
        # W = window.hamming(N)
        T = 1/44100
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal):
        x, y = self.calcFFT(signal)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
        plt.show()
