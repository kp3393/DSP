# -- Exercise 2.6 Triangle and square waves have odd harmonics only; the sawtooth
# -- wave has both even and odd harmonics. The harmonics of the square
# -- and sawtooth waves drop off in proportion to 1/ f ; the harmonics of the triangle
# -- wave drop off like 1/ f 2. Can you find a waveform that has even and
# -- odd harmonics that drop off like 1/ f 2?
# -- Hint: There are two ways you could approach this: you could construct the
# -- signal you want by adding up sinusoids, or you could start with a signal
# -- that is similar to what you want and modify it.

# -- We want a signal which has all the harmonics like sawtooth and whose spectrum falls like 1/f2
# -- as in the case for triangle wave

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt
import math

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

PI2 = 2*math.pi

signal = thinkdsp.SawtoothSignal(freq=500)
wave = signal.make_wave(duration=0.5, framerate=20000)
spectrum = wave.make_spectrum()
# spectrum.plot(color = "gray")
# plt.xlabel('Frequency (Hz)')
# plt.savefig('01_sawtooth_spectrum.png')
# plt.show()

def spectfreq_divider(spectrum):
    spectrum.hs /= spectrum.fs
    spectrum.hs[0] = 0

spectfreq_divider(spectrum)
# spectrum.scale(500)
# spectrum.plot(color = "red")
# plt.xlabel('Frequency (Hz)')
# plt.savefig('02_comparison.png')
# plt.show()

req_wave = spectrum.make_wave()
req_wave.segment(duration = 0.01).plot()
plt.xlabel('Time (Sec)')
plt.savefig('03_required_wave.png')
plt.show()
