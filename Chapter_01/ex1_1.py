from __future__ import print_function, division

#matplotlib inline

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

#Instantiate cosine and sine signals.

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

#Plot the sine and cosine signals. By default, plot plots three periods.

cos_sig.plot()

# plt.xlabel('Time (s)')
# plt.show()
#thinkplot.config(xlabel='Time (s)')

#Notice that the frequency of the sine signal is doubled, so the period is halved.

sin_sig.plot()

# plt.xlabel('Time (s)')
# plt.show()
#thinkplot.config(xlabel='Time (s)')

mix = sin_sig + cos_sig
mix

# Waves
# A Signal represents a mathematical function defined for all values of time.
# If you evaluate a signal at a sequence of equally-spaced times, the result is a Wave.
# framerate is the number of samples per second.

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave

#IPython provides an Audio widget that can play a wave.

from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)
audio

#Wave also provides make_audio(), which does the same thing:

wave.make_audio()

#The ys attribute is a NumPy array that contains the values from the signal.
#The interval between samples is the inverse of the framerate.

print('Number of samples', len(wave.ys))
print('Timestep in ms', 1 / wave.framerate * 1000)

#Signal objects that represent periodic signals have a period attribute.
#Wave provides segment, which creates a new wave.
#So we can pull out a 3 period segment of this wave.

period = mix.period
segment = wave.segment(start=0, duration=period*3)
period

#Wave provides plot

segment.plot()
# plt.xlabel('Time (s)')
# plt.show()

#normalize scales a wave so the range doesn't exceed -1 to 1.
#apodize tapers the beginning and end of the wave so it doesn't click when you play it.
wave.normalize()
wave.apodize()
wave.plot()
# plt.xlabel('Time (s)')
# plt.show()

#You can write a wave to a WAV file.
#wave.write('temp.wav')


#read_wave reads WAV files. The WAV examples in the book are from freesound.org.

wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
wave.make_audio()

start = 1.2
duration = 0.6
segment = wave.segment(start, duration)
segment.plot()
plt.xlabel('Time (s)')
plt.show()
