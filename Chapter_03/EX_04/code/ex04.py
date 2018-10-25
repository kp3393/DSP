# Exercise 3.4 In musical terminology, a “glissando” is a note that slides from
# one pitch to another, so it is similar to a chirp.
# Find or make a recording of a glissando and plot a spectrogram of the first
# few seconds. One suggestion: George Gershwin’s Rhapsody in Blue starts
# with a famous clarinet glissando, which you can download from http://
# archive.org/details/rhapblue11924.
from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

import math
PI2 = 2 * math.pi

wave = thinkdsp.read_wave("72475__rockwehrmann__glissup02.wav")
wave.make_audio()
wave.make_spectrogram(512).plot(high=5000)
plt.xlabel('Time (Sec)')
plt.ylabel('Frequency (Hz)')
plt.savefig('01_glissando_Spectrum.png')
plt.show()
