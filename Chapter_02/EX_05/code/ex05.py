# -- Exercise 2.5: Write a function that takes a Spectrum as a parameter and
# -- modifies it by dividing each element of hs by the corresponding frequency
# -- from fs. Hint: since division by zero is undefined, you might want to set
# -- spectrum.hs[0] = 0.
# -- Test your function using a square, triangle, or sawtooth wave.
# -- 1. Compute the Spectrum and plot it.
# -- 2. Modify the Spectrum using your function and plot it again.
# -- 3. Use Spectrum.make_wave to make a Wave from the modified Spectrum,
# -- and listen to it. What effect does this operation have on the
# -- signal?

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

# -- Write a function that takes a Spectrum as a parameter and
# -- modifies it by dividing each element of hs by the corresponding frequency
# -- from fs. Hint: since division by zero is undefined, you might want to set
# -- spectrum.hs[0] = 0.

def spectfreq_divider(spectrum):
    spectrum.hs /= spectrum.fs
    spectrum.hs[0] = 0

# -- trianglewave Plot
# wave = thinkdsp.TriangleSignal(freq=440).make_wave(duration = 0.5)
# wave.make_audio()
# wave.write('01_triangle_wave_before.wav')
#
# spectrum = wave.make_spectrum()
# spectrum.plot(high=10000,color = 'gray')
# # plt.xlabel('Frequency (Hz)')
# # plt.savefig('01_triangle_spectrum.png')
# # plt.show()
#
# spectfreq_divider(spectrum)
# spectrum.scale(440)
# spectrum.plot(high=10000)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('01_triangle_spect_comparison.png')
# plt.show()
#
# wave2 = spectrum.make_wave()
# wave2.make_audio()
# wave2.write('01_triangle_wave_after.wav')

# -- squarewave Plot
wave = thinkdsp.SquareSignal(freq=440).make_wave(duration = 0.5)
wave.make_audio()
wave.write('02_square_wave_before.wav')

spectrum = wave.make_spectrum()
spectrum.plot(high=10000,color = 'gray')
# plt.xlabel('Frequency (Hz)')
# plt.savefig('01_triangle_spectrum.png')
# plt.show()

spectfreq_divider(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
plt.xlabel('Frequency (Hz)')
plt.savefig('02_square_spect_comparison.png')
plt.show()

wave2 = spectrum.make_wave()
wave2.make_audio()
wave2.write('02_square_wave_after.wav')
