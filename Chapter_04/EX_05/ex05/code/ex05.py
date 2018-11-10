''' The algorithm in this chapter for generating pink noise is conceptually simple but computationally expensive.
There are more efficient alternatives, like the Voss-McCartney algorithm.
Research this method, implement it, compute the spectrum of the result, and confirm that it has the desired relationship between power and frequency.'''

''' Refer the ex05cwt.py for detailed exlanation'''

import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def voss(nrows, ncols = 16):
    array = np.empty((nrows,ncols))
    array.fill(np.nan)
    array[0,:] = np.random.random(ncols)
    array[:,0] = np.random.random(nrows)
    # changes in n rows
    # random selection of columns
    cols = np.random.geometric(0.5, nrows)
    cols[cols >= ncols] = 0
    # randomly select row from columns
    rows = np.random.randint(nrows, size = nrows)
    array[rows,cols] = np.random.random(nrows)
    #replacing NaN with values
    #numpy array to pandas dataframe
    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    total = df.sum(axis = 1)

    return total.values

def bartlett_method(wave, seg_length=512):
    spectro = wave.make_spectrogram(seg_length)         # Make a spectrogram of the wave input
    spectrums = spectro.spec_map.values()               # Access the spectrum values. spec_map.values() access the values in the dictionary
    psds = [spectrum.power for spectrum in spectrums]
    hs = np.sqrt(sum(psds)/len(psds))
    fs = next(iter(spectrums)).fs
    spectrum = thinkdsp.Spectrum(hs, fs, wave.framerate)
    return spectrum

# Testing the above implementation
testpink = voss(11025)
np.savetxt('01_testpink.txt',testpink)

wave = thinkdsp.Wave(testpink)
wave.unbias()
wave.normalize()
wave.plot()
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.savefig("01_wave.png")
plt.show()

spectrum = wave.make_spectrum()
spectrum.hs[0] = 0
spectrum.plot_power()
plt.loglog()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.savefig("02_spectrum")
plt.show()
print(spectrum.estimate_slope().slope)

seg_length = 64 * 1024
iters = 100
wave = thinkdsp.Wave(voss(seg_length * iters))
print(len(wave))

spectrum = bartlett_method(wave, seg_length=seg_length)
spectrum.hs[0] = 0
print(len(spectrum))
spectrum.plot_power()
plt.loglog()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.savefig("03_spectrum_bartlett")
plt.show()
print(spectrum.estimate_slope().slope)
