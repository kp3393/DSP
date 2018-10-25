# -- Exercise 3.5 A trombone player can play a glissando by extending the trombone
# -- slide while blowing continuously. As the slide extends, the total length
# -- of the tube gets longer, and the resulting pitch is inversely proportional to
# -- length.
# -- Assuming that the player moves the slide at a constant speed, how does
# -- frequency vary with time?
# -- Write a class called TromboneGliss that extends Chirp and provides
# -- evaluate. Make a wave that simulates a trombone glissando from C3 up
# -- to F3 and back down to C3. C3 is 262 Hz; F3 is 349 Hz.
# -- Plot a spectrogram of the resulting wave. Is a trombone glissando more like
# -- a linear or exponential chirp?

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

import math
PI2 = 2 * math.pi

class TromboneGliss(thinkdsp.Chirp):
    def evaluate(self,ts):
        # -- Frequency is inversely proportional to the length
        l1, l2 = 1.0/self.start, 1.0/self.end
        lengths = np.linspace(l1,l2,len(ts)-1)
        freqs = 1/lengths
        return self._evaluate(ts,freqs)

# -- Going from C3 to F3.
signal = TromboneGliss(262, 349)
wave1 = signal.make_wave(duration = 1)
wave1.apodize()
wave1.make_audio()
wave1.write("Trombone_c3_to_f3.wav")
wave1.make_spectrum().plot(high = 600)
plt.xlabel('Frequency (Hz)')
plt.savefig('01_up_spectrum.png')
plt.show()


signal = TromboneGliss(349, 262)
wave2 = signal.make_wave(duration = 1)
wave2.apodize()
wave2.make_audio()
wave2.write("Trombone_f3_to_c3.wav")
wave2.make_spectrum().plot(high = 600)
plt.xlabel('Frequency (Hz)')
plt.savefig('02_down_spectrum.png')
plt.show()

wave = wave1 | wave2
wave.make_audio()
wave.write("Trombone.wav")

sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
plt.xlabel('Time (Sec)')
plt.ylabel('Frequency (Hz)')
plt.savefig('Spectrogram.png')
plt.show()
