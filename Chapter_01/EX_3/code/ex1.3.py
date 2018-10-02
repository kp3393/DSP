# -- Exercise 1.3 Synthesize a compound signal by creating SinSignal and
# -- CosSignal objects and adding them up. Evaluate the signal to get a Wave,
# -- and listen to it. Compute its Spectrum and plot it. What happens if you add
# -- frequency components that are not multiples of the fundamental?

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# -- Synthesize a compound signal by creating SinSignal and
# -- CosSignal objects and adding them up.
cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)
mix = cos_sig + sin_sig
# mix.plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_mix.png')
# plt.show()

# -- Evaluate the signal to get a Wave,
# -- and listen to it. Compute its Spectrum and plot it.
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave.normalize()
wave.apodize()
# wave.write("mix.wav")
spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel("Hertz (Hz)")
# plt.savefig("02_mix_spectrum.png")
# plt.show()

# -- What happens if you add
# -- frequency components that are not multiples of the fundamental?
other_sig = thinkdsp.SinSignal(freq=150, amp=0.75, offset=0)
mix = cos_sig + sin_sig + other_sig
mix.plot()
plt.xlabel('Time (s)')
plt.savefig('03_other_mix.png')
plt.show()
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave.normalize()
wave.apodize()
wave.write("other_mix.wav")
spectrum = wave.make_spectrum()
spectrum.plot()
plt.xlabel("Hertz (Hz)")
plt.savefig("04_mix_other_spectrum.png")
plt.show()
