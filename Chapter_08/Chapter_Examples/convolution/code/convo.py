from __future__ import print_function, division
import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import scipy.signal
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)
PI2 = 2 * np.pi
GRAY = '0.7'

'''SMOOTHING'''
def smooth(n,segment):
    window = np.ones(n)                                                         # create a window of ones for the given window size
    window /=sum(window)                                                        # Normalise it. 

    ys = segment.ys                                                             # get the y values of the samples.
    N = len(ys)                                                                 # N is length of ys.
    padded = thinkdsp.zero_pad(window,N)                                        # Since the window size and the sample size are different we need to do zerom padding so that multiplication is possible.
    smoothed = np.zeros(N)                                                      # smoothed is list which will consist of all the smoothened values.

    for i in range(N):
        smoothed[i] = sum(padded * ys)
        padded = np.roll(padded,1)
    return smoothed

signal = thinkdsp.SquareSignal(freq=440)
wave = signal.make_wave(duration=1, framerate=44100)
segment = wave.segment(duration=0.01)

n = input('Enter the window size:')
n = int(n)

ys2 = smooth(n,segment)                                                         # ys2 is the smoothened signal from the above logic.

window = np.ones(n)
window /= sum(window)

convolved = np.convolve(segment.ys, window, mode = 'valid')
smooth2 = thinkdsp.Wave(convolved, framerate=wave.framerate)


# plt.plot(segment.ts, ys2, color = 'red',label = 'smoothning algorithm')
# plt.plot(smooth2.ts, smooth2.ys, color = 'black',label = 'numpy convolution')
# plt.legend()
# plt.legend(loc = 'upper left',prop={'size':8})
# plt.show() 
# plt.savefig('01_algorithm_vs_numpy.png')

''' Frequency domain'''
spectrum_wave = wave.make_spectrum()
# spectrum_wave.plot(color = 'gray', label = 'Wave spectrum')

convolved = np.convolve(wave.ys, window, mode = 'same')
smooth2 = thinkdsp.Wave(convolved, framerate=wave.framerate)

spectrum_convo = smooth2.make_spectrum()
# spectrum_convo.plot(color = 'blue', label = 'Convolved spectrum')

# plt.legend()
# plt.legend(loc = 'upper right',prop={'size':8})
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.savefig('02_wave_convolved_spectrum.png')
# plt.show()

amps = spectrum_wave.amps
amps2 = spectrum_convo.amps
ratio = amps2/amps
ratio[amps<560] = 0
# thinkplot.plot(ratio)
# plt.savefig('03_amplitude_ratio.png')
# plt.show()

'''Convolution in TIME is multiplication in Freq'''
N = len(wave.ys)
padded =  thinkdsp.zero_pad(window,N)
dft_window = np.fft.rfft(padded)
# thinkplot.plot(abs(dft_window),label = 'Window_Spectrum')
# plt.savefig('04_convo_freq.png')
# plt.show()

'''Gaussian filter/window'''
gauss = scipy.signal.gaussian(M=11,std=2)
gauss /= sum(gauss)

gauss = thinkdsp.zero_pad(gauss,N)

gauss_wave = thinkdsp.Wave(gauss, framerate=wave.framerate)
# gaussain_spectrum = np.fft.rfft(gauss)
# thinkplot.plot(abs(gaussain_spectrum),label='Gaussain_Spectrum')
# plt.legend()
# plt.savefig('05_Gaussian_vs_Boxcar.png')
# plt.show()
gaussian_conv = np.convolve(wave.ys,gauss, mode = 'same')
gaussian_conv_spec = thinkdsp.Wave(gaussian_conv,framerate=wave.framerate)
gaussian_conv_spec = gaussian_conv_spec.make_spectrum() 

amps = spectrum_wave.amps
amps2 = gaussian_conv_spec.amps
ratio = amps2/amps
ratio[amps<560] = 0

thinkplot.plot(ratio)
# plt.savefig('06_Gaussian_filter.png')
# plt.show()
