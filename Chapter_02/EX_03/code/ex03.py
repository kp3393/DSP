# -- Exercise 2.3 Make a square signal at 1100 Hz and make a wave that samples
# -- it at 10000 frames per second. If you plot the spectrum, you can see that
# -- most of the harmonics are aliased. When you listen to the wave, can you
# -- hear the aliased harmonics?

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

# -- Square wave
square = thinkdsp.SquareSignal(1100).make_wave(duration = 0.5, framerate = 10000)
# square.make_spectrum().plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('01_square.png')
# plt.show()

# -- Audio file
square.make_audio()
square.write('01_aliased_square.wav')
