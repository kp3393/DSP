# Exercise: In a noise signal, the mixture of frequencies changes over time.
# In the long run, we expect the power at all frequencies to be equal, but in any sample, the power at each frequency is random.
# To estimate the long-term average power at each frequency, we can break a long signal into segments, compute the power spectrum for each segment, and then compute the average across the segments.
# You can read more about this algorithm at http://en.wikipedia.org/wiki/Bartlett's_method.
# Implement Bartlett's method and use it to estimate the power spectrum for a noise wave. Hint: look at the implementation of make_spectrogram.

# -- Here we will get spectrums of segments from Spectrogram. If we have  look at the spectrogram code we will notice
# -- that we take segments and then compute their spectrumself.
# -- spec_map has those spectrums.
# -- Once you get these spectrums you square their values --> divide by the length of the spectrum --> take a square root of itself.
# -- This is called root mean square method.

from __future__ import print_function, division

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

# -- Ocean wave
wave = thinkdsp.read_wave("132736__ciccarelli__ocean-waves.wav")
segment = wave.segment(start=1.5, duration=1.0)
spectrum = segment.make_spectrum()

segment2 = wave.segment(start=2.5, duration=1.0)
spectrum2 = segment2.make_spectrum()
# spectrum.plot_power(color="Blue")
# spectrum2.plot_power(color="red")
#
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Power")
# plt.loglog()
# plt.savefig("01_ocean_waves_power_spectrum.png")
# plt.show()

def bartlett_method(wave, seg_length=512):
    spectro = wave.make_spectrogram(seg_length)                                 # Make a spectrogram of the wave input
    spectrums = spectro.spec_map.values()                                       # Access the spectrum values. spec_map.values() access the values in the dictionary
    psds = [spectrum.power for spectrum in spectrums]
    hs = np.sqrt(sum(psds)/len(psds))
    fs = next(iter(spectrums)).fs
    spectrum = thinkdsp.Spectrum(hs, fs, wave.framerate)
    return spectrum

psd = bartlett_method(segment)
psd2 = bartlett_method(segment2)

psd.plot_power()
psd2.plot_power(color='Red')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.loglog()
plt.savefig("02_ocean_waves_power_spectrum_Bartlett.png")
plt.show()
