# -- Exercise 4.1 “A Soft Murmur” is a web site that plays a mixture of natural
# -- noise sources, including rain, waves, wind, etc. At http://asoftmurmur.
# -- com/about/ you can find their list of recordings, most of which are at http:
# -- //freesound.org.
# -- Download a few of these files and compute the spectrum of each signal.
# -- Does the power spectrum look like white noise, pink noise, or Brownian
# -- noise? How does the spectrum vary over time?

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
# wave = thinkdsp.read_wave("132736__ciccarelli__ocean-waves.wav")
# wave.make_audio()

# -- Signal Plot
# wave.plot()
# plt.xlabel("Time (Hz)")
# plt.ylabel("Amplitude")
# plt.savefig("01_ocean_waves.png")
# plt.show()

# -- Spectrum Plot
# segment = wave.segment(start = 1.5, duration = 1.0)
# spectrum = segment.make_spectrum()
# spectrum.plot_power()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Power")
# plt.loglog()
# plt.savefig("01_ocean_waves_spectrum.png")
# plt.show()

# -- White noise
wave = thinkdsp.read_wave("White_Noise.wav")

# -- Signal Plot
# wave.plot()
# plt.xlabel("Time (Hz)")
# plt.ylabel("Amplitude")
# plt.savefig("02_white_noise.png")
# plt.show()

# -- Spectrum Plot
#segment = wave.segment(start = 1.5, duration = 1.0)
spectrum = wave.make_spectrum()
spectrum.plot_power()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.loglog()
plt.savefig("02_white_noise_spectrum.png")
plt.show()

integ = spectrum.make_integrated_spectrum()
integ.plot_power(high = 5000)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Cummalative fraction of total power")
plt.savefig("02_integrated_spectrum.png")
plt.show()
