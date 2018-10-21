# -- Exercise 3.1 Run and listen to the examples in chap03.ipynb, which is in
# -- the repository for this book, and also available at http://tinyurl.com/
# -- thinkdsp03.
# -- In the leakage example, try replacing the Hamming window with one of
# -- the other windows provided by NumPy, and see what effect they have on
# -- leakage. See http://docs.scipy.org/doc/numpy/reference/routines.
# -- window.html

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# -- Chirp
# -- Make a linear chirp from A3 to A5.
signal = thinkdsp.Chirp(start=220, end=880)
wave1 = signal.make_wave(duration=2)
# wave1.make_audio()
# wave1.write("01_chirp.wav")

# -- Here's what the waveform looks like near the beginning.
# wave1.segment(start=0, duration=0.01).plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_chirp_beginning.png')
# plt.show()

# -- And near the end.
# wave1.segment(start=0.9, duration=0.01).plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_chirp_end.png')
# plt.show()

# -- Complete linear chip plot
# wave1.plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_chirp.png')
# plt.show()

# -- Here's an exponential chirp with the same frequency range and duration.
# signal = thinkdsp.ExpoChirp(start=220, end=880)
# wave2 = signal.make_wave(duration=2)
# wave2.make_audio()
# wave2.write("02_expchirp.wav")

# wave2.plot()
# plt.xlabel('Time (s)')
# plt.savefig('02_expchirp.png')
# plt.show()


# -- Leakage
# Spectral leakage is when some of the energy at one frequency appears at another frequency (usually nearby).
# Let's look at the effect of leakage on a sine signal (which only contains one frequency component).
signal = thinkdsp.SinSignal(freq=440)

# -- If the duration is an integer multiple of the period, the beginning and end of the segment line up,
# -- and we get minimal leakage.
duration = signal.period*30
wave = signal.make_wave(duration)
# wave.plot()
# plt.xlabel('Time (s)')
# plt.savefig('03_sinsignal.png')
# plt.show()

# spectrum = wave.make_spectrum()
# spectrum.plot(high = 880)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('03_sinsignal_spectrum.png')
# plt.show()

# -- If the duration is not a multiple of a period, the leakage is pretty bad.
# duration = signal.period * 30.25
# wave = signal.make_wave(duration)
# wave.plot()
# plt.xlabel('Time (s)')
# plt.savefig('04_sinsignal_leak.png')
# plt.show()

spectrum = wave.make_spectrum()
# spectrum.plot(high = 880)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('04_sinsignal_leak_spectrum.png')
# plt.show()

# -- Windowing helps (but notice that it reduces the total energy).
# wave.hamming()
# spectrum = wave.make_spectrum()
# spectrum.plot(high = 880)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('04_sinsignal_hamming_spectrum.png')
# plt.show()

# -- Spectrogram
# -- If you blindly compute the DFT of a non-periodic segment, you get "motion blur".
signal = thinkdsp.Chirp(start=220, end=440)
wave = signal.make_wave(duration=1)
spectrum = wave.make_spectrum()
# spectrum.plot(high=700)
# plt.xlabel('Frequency (Hz)')
# plt.savefig('06_Chirp_spectrum.png')
# plt.show()


# -- A spectrogram is a visualization of a short-time DFT that lets you see how the spectrum varies over time.
def plot_spectrogram(wave, seg_length):
    spectrogram = wave.make_spectrogram(seg_length)
    print('Time resolution (s)', spectrogram.time_res)
    print('Frequency resolution (Hz)', spectrogram.freq_res)
    spectrogram.plot(high=700)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Time (Sec)')
    plt.savefig('06_Chirp_better_time.png')
    plt.show()

signal = thinkdsp.Chirp(start=220, end=440)
wave = signal.make_wave(duration=1, framerate=11025)
#plot_spectrogram(wave, 512)

# -- If you increase the segment length, you get better frequency resolution, worse time resolution.
#plot_spectrogram(wave, 1024)

# -- If you decrease the segment length, you get better time resolution, worse frequency resolution.
plot_spectrogram(wave, 256)
