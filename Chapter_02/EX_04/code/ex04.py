# -- Exercise 2.4 If you have a spectrum object, spectrum, and print the first few
# -- values of spectrum.fs, you’ll see that they start at zero. So spectrum.hs[0]
# -- is the magnitude of the component with frequency 0. But what does that
# -- mean?
# -- Try this experiment:
# -- 1. Make a triangle signal with frequency 440 and make a Wave with duration
# -- 0.01 seconds. Plot the waveform.
# -- 2. Make a Spectrum object and print spectrum.hs[0]. What is the amplitude
# -- and phase of this component?
# -- 3. Set spectrum.hs[0] = 100. What effect does this operation have on
# -- the waveform? Hint: Spectrum provides a method called make_wave
# -- that computes the Wave that corresponds to the Spectrum.

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

# -- 1. Make a triangle signal with frequency 440 and make a Wave with duration
# -- 0.01 seconds. Plot the waveform.
triangle = thinkdsp.TriangleSignal(440).make_wave(duration = 0.01, framerate = 10000)
# triangle.plot()
# plt.xlabel('Time (Sec)')
# plt.savefig('01_triangle.png')
# plt.show()

# -- 2. Make a Spectrum object and print spectrum.hs[0]. What is the amplitude
# -- and phase of this component?
spect = triangle.make_spectrum()
# with open('spectrum.txt','w') as fhandle:
#     for i in range (len(spect.hs)):
#         output = str(spect.hs[i]) + '\n'
#         fhandle.write(output)

# -- 3. Set spectrum.hs[0] = 100. What effect does this operation have on
# -- the waveform? Hint: Spectrum provides a method called make_wave
# -- that computes the Wave that corresponds to the Spectrum.
# spect.hs[0] = 100
# spect.make_wave().plot()
# plt.xlabel('Time (Sec)')
# plt.savefig('02_manipulated_triangle.png')
# plt.show()

# -- comparison
triangle = thinkdsp.TriangleSignal(440).make_wave(duration = 0.01, framerate = 10000)
triangle.plot(color = 'gray')
spect.hs[0] = 100
spect.make_wave().plot()
plt.xlabel('Time (Sec)')
plt.savefig('03_comparison.png')
plt.show()
