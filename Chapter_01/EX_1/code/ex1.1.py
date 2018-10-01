# -- Exercise 1: Run the code in the following cells to create a Signal with two frequency components, and then create a Wave that contains a half-second sample from the Signal.
# -- Add code to compute and plot the Spectrum of this Wave.
# -- Then add another Signal to the mix, recompute the Wave and look at the Spectrum.
# -- Code

# -- cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
# -- sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)
# -- mix = cos_sig + sin_sig
# -- mix.plot()
# -- wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
# -- wave.plot()

from __future__ import print_function, division

# -- matplotlib inline

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)
mix = cos_sig + sin_sig
# mix.plot()
# plt.xlabel('Time (s)')
# plt.savefig('mix.png')
# plt.show()

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
# wave.plot()
# plt.xlabel('Time (s)')
# plt.savefig('ex1_1_wave.png')
# plt.show()

spectrum = wave.make_spectrum()
spectrum.plot()
plt.xlabel('Hertz (Hz)')
plt.savefig('ex1_1_Spectrum.png')
plt.show()
