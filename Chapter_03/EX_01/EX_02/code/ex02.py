# Exercise 3.2 Write a class called SawtoothChirp that extends Chirp and
# overrides evaluate to generate a sawtooth waveform with frequency that
# increases (or decreases) linearly.

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
class SawtoothChirp(thinkdsp.Chirp):
    # So we need a sawtoothwave form with frequencz that increases or decreases with time.
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
signal = SawtoothChirp(start = 220, end = 880)
wave = signal.make_wave(duration = 1, framerate = 10000)
wave.apodize()
# wave.make_audio()
# wave.write("01_SawtoothChirp.wav")

# -- Plot of signal
# wave.plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_SawtoothChirp.png')
# plt.show()

# -- Spectrum of the signal
spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('01_SawoothChirp_Spectrum.png')
# plt.show()

# -- Spectrogram of the signal
sp = wave.make_spectrogram(1024)
sp.plot()
# spectrum.plot(high=700)
plt.xlabel('Frequency (Hz)')
plt.savefig('01_SawoothChirp_Spectrogram.png')
plt.show()
