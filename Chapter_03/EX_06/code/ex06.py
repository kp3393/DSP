# -- Exercise 3.6 Make or find a recording of a series of vowel sounds and look
# -- at the spectrogram. Can you identify different vowels?

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

import math

signal = thinkdsp.read_wave("87778__marcgascon7__vocals.wav")
signal.make_audio()
# signal.plot()
# plt.xlabel("Time(Sec)")
# plt.ylabel("Amplitude")
# plt.savefig('01_signal.png')
# plt.show()

signal.make_spectrogram(1024)#.plot(high=1000)
# plt.xlabel("Time (Sec)")
# plt.ylabel("Frequency (Hz)")
# plt.savefig('02_signal_spectrogram.png')
# plt.show()

signal.make_spectrum(1024)#.plot(high=1000)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.savefig('03_signal_spectrum.png')
# plt.show()

high = 1000
thinkplot.preplot(5)

segment = signal.segment(start=1, duration=0.25)
# segment.make_spectrum().plot(high=high)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.savefig('04_ah_segment.png')
# plt.show()

segment = signal.segment(start=2.2, duration=0.25)
segment.make_spectrum().plot(high=high)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.savefig('05_eh_segment.png')
plt.show()

segment = signal.segment(start=3.5, duration=0.25)
segment.make_spectrum().plot(high=high)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.savefig('06_ih_segment.png')
plt.show()

segment = signal.segment(start=5.1, duration=0.25)
segment.make_spectrum().plot(high=high)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.savefig('07_oh_segment.png')
plt.show()

segment = signal.segment(start=6.5, duration=0.25)
segment.make_spectrum().plot(high=high)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.savefig('08_oo_segment.png')
plt.show()
