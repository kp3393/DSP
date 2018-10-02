# Exercise 1.4 Write a function called stretch that takes a Wave and a stretch
# factor and speeds up or slows down the wave by modifying ts and
# framerate. Hint: it should only take two lines of code.

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

def stretch (wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')
wave.normalize()
wave.plot()
plt.xlabel('Time (s)')
plt.savefig('01_wave_before.png')
plt.show()

stretch(wave,2)
wave.plot()
plt.xlabel('Time (s)')
plt.savefig('02_wave_after.png')
plt.show()
wave.write('wave_stretched.wav')
