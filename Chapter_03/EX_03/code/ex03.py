# -- Exercise 3.3 Make a sawtooth chirp that sweeps from 2500 to 3000 Hz, then
# -- use it to make a wave with duration 1 s and frame rate 20 kHz. Draw a
# -- sketch of what you think the spectrum will look like. Then plot the spectrum
# -- and see if you got it right.
from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

import math
PI2 = 2 * math.pi

# -- Class defination
# -- Let us define a class for sawtooth waveform
class SawtoothChirp(thinkdsp.Chirp):
    def _evaluate(self,ts,freqs):
        dts = np.diff(ts)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        phases = np.insert(phases, 0, 0)
        cycles = phases/PI2
        frac, _ = frac,_ =np.modf(cycles)
        ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
        return ys

# -- Sound of such a waveform
signal = SawtoothChirp(start = 2500, end = 3000)
wave = signal.make_wave(duration = 1, framerate = 20000)
wave.apodize()
wave.make_audio()
wave.write("01_SawtoothChirp.wav")

# How does the spectrum looks like?
wave.make_spectrum().plot()
plt.xlabel('Frequency (Hz)')
plt.savefig('01_SawoothChirp_Spectrum.png')
plt.show()
