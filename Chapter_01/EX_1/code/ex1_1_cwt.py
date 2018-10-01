# -- Exercise solutions for ThinkDSP by Allen Downey.
# -- Chapter 1
# -- Exercise 1.1 : If you have Jupyter, load chap01.ipynb, read through it, and
# -- run the examples. You can also view this notebook at http://tinyurl.com/thinkdsp01.

from __future__ import print_function, division

# -- matplotlib inline

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# -- Instantiate cosine and sine signals.
cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

# -- Plot the sine and cosine signals. By default, plot plots three periods.
# cos_sig.plot()
# plt.xlabel('Time (s)')
# plt.savefig('cos_sig.png')
# plt.show()

# -- Notice that the frequency of the sine signal is doubled, so the period is halved.
# sin_sig.plot()
# plt.xlabel('Time (s)')
# plt.savefig('sin_sig.png')
# plt.show()

mix = sin_sig + cos_sig
mix

# -- WAVES
# -- A Signal represents a mathematical function defined for all values of time.
# -- If you evaluate a signal at a sequence of equally-spaced times, the result is a Wave.
# -- framerate is the number of samples per second.
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave

# -- IPython provides an Audio widget that can play a wave.
from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)
audio

# -- Wave also provides make_audio(), which does the same thing:
wave.make_audio()

# -- The ys attribute is a NumPy array that contains the values from the signal.
# -- The interval between samples is the inverse of the framerate.
print('Number of samples', len(wave.ys))
print('Timestep in ms', 1 / wave.framerate * 1000)

# -- Signal objects that represent periodic signals have a period attribute.
# -- Wave provides segment, which creates a new wave.
# -- So we can pull out a 3 period segment of this wave.
period = mix.period
segment = wave.segment(start=0, duration=period*3)
period

# -- Wave provides plot
segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('segment.png')
# plt.show()

# -- normalize scales a wave so the range doesn't exceed -1 to 1.
# -- apodize tapers the beginning and end of the wave so it doesn't click when you play it.
wave.normalize()
wave.apodize()
# wave.plot()
# plt.xlabel('Time (s)')
# plt.savefig('wave.png')
# plt.show()

# -- You can write a wave to a WAV file.
# wave.write('temp.wav')

# -- read_wave reads WAV files. The WAV examples in the book are from freesound.org.
wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
wave.make_audio()

# -- Pull out a segment of this recording where the pitch is constant.
# -- When we plot the segment, we can't see the waveform clearly, but we can see the "envelope", which tracks the change in amplitude during the segment.
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('segment_violin.png')
# plt.show()

# -- SPECTRUMS
# -- Wave provides make_spectrum, which computes the spectrum of the wave.
spectrum = segment.make_spectrum()

# -- Spectrum provides plot
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('spectrum.png')
# plt.show()

# -- The frequency components above 10 kHz are small.
# -- We can see the lower frequencies more clearly by providing an upper bound:
# spectrum.plot(high=10000)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('spectrum_freq_upper_bound.png')
# plt.show()

# -- Spectrum provides low_pass, which applies a low pass filter;
# -- that is, it attenuates all frequency components above a cutoff frequency.
spectrum.low_pass(3000)
# spectrum.plot(high=10000)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('spectrum_lpf.png')
# plt.show()

# -- We can convert the filtered spectrum back to a wave:
filtered = spectrum.make_wave()

# -- And then normalize it to the range -1 to 1.
filtered.normalize()

# -- Before playing it back, I'll apodize it (to avoid clicks).
filtered.apodize()
# filtered.plot()
# plt.xlabel('Time (s)')
# plt.savefig('filtered.png')
# plt.show()
filtered.write("Filtered.wav")

# -- Do the same with the original segment.
segment.normalize()
segment.apodize()
segment.write("segment.wav")
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('Original_seg.png')
# plt.show()

# -- Listen to the original segment and the filtered version.
segment.make_audio()
filtered.make_audio()














# thinkplot.config(xlabel='Frequency (Hz)')
