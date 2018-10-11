#Exercise 2.1 If you use Jupyter, load chap02.ipynb and try out the examples.
#You can also view the notebook at http://tinyurl.com/thinkdsp02.

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# -- Waveforms and harmonics
# -- Create a triangle signal and plot a 3 period segment
signal = thinkdsp.TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('01_Triangle_wave.png')
# plt.show()

# -- Make a wave and play it.
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
# wave.make_audio()
# wave.write('01_audio_triangular_wave.wav')

# -- Compute its spectrum and plot it.
spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('02_Triangular_spectrum.png')
# plt.show()

# -- Make a square signal and plot a 3 period segment.
signal = thinkdsp.SquareSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('03_Square_wave.png')
# plt.show()

# -- Make a wave and play it.
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()
# wave.write('02_audio_square_wave.wav')

# -- Compute its spectrum and plot it.
spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('04_square_spectrum.png')
# plt.show()

# -- Create a sawtooth signal and plot a 3 period segment.
signal = thinkdsp.SawtoothSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('05_Sawtooth_wave.png')
# plt.show()

# -- Make a wave and play it.
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
# wave.make_audio()
# wave.write('03_audio_sawtooth_wave.wav')

# -- Compute its spectrum and plot it.
spectrum = wave.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('05_sawtooth_spectrum.png')
# plt.show()

# -- ALiasing
# -- Make a cosine signal at 4500 Hz, make a wave at framerate 10 kHz, and plot 5 periods.
framerate = 10000
signal = thinkdsp.CosSignal(4500)
duration = signal.period*5
segment = signal.make_wave(duration, framerate=framerate)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('06_cos_wave.png')
# plt.show()

# -- Make a cosine signal at 5500 Hz, make a wave at framerate 10 kHz, and plot the same duration.
# -- With framerate 10 kHz, the folding frequency is 5 kHz, so a 4500 Hz signal and a 5500 Hz signal look exactly the same.
signal1 = thinkdsp.CosSignal(550)
segment = signal.make_wave(duration, framerate=framerate)
# segment.plot()
# plt.xlabel('Time (s)')
# plt.savefig('07_cos_wave_5500kHz.png')
# plt.show()

# plt.xlabel('Time (s)')
# plt.savefig('08_combined_cos_wave.png')
# plt.show()


# -- Make a triangle signal and plot the spectrum. See how the harmonics get folded.
signal = thinkdsp.TriangleSignal(1100)
segment = signal.make_wave(duration=0.5, framerate=10000)
spectrum = segment.make_spectrum()
# spectrum.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('09_triangular_aliasing_spectrum.png')
# plt.show()

# -- Amplitude and phase
# -- Make a sawtooth wave.
signal = thinkdsp.SawtoothSignal(500)
wave = signal.make_wave(duration = 1, framerate = 10000)
segment = wave.segment(duration = 0.005)
# segment.plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('10_sawtooth_amp&phase.png')
# plt.show()

# -- play the audio
wave.make_audio()
# wave.write('05_audio_sawtoot_amp&phase.wav')

# -- Extract wave array and compute real FFT
hs = np.fft.rfft(wave.ys)
# with open("rfft.txt","w") as fhandle:
#     for i in range(len(hs)):
#         output = str(hs[i])+"\n"
#         fhandle.write(output)

# -- compute the frequency that match up with the the elements of fft.
n = len(wave.ys)
d = 1/wave.framerate
fs = np.fft.rfftfreq(n, d)
# with open("rfftfreq.txt","w") as fhandle:
#     for i in range(len(fs)):
#         output = str(fs[i])+"\n"
#         fhandle.write(output)

# -- plot the phase vs the frequency
angle = np.angle(hs)
# plt.plot(fs,angle)
# plt.xlabel("Frequency (Hz)")
# plt.savefig('11_angle_vs_freq.png')
# plt.show()

# -- phase plot
# -- shuffle the phases
import random
random.shuffle(angle)
# plt.plot(fs, angle)
# plt.xlabel("Frequency (Hz)")
# plt.savefig('12_shuffleangle_vs_freq.png')
# plt.show()


# Put the shuffled phases back into the spectrum.
# Each element in hs is a complex number with magitude A and phase phi,
# with which we can compute A e^{i*phi}
i = complex(0,1)
spectrum=wave.make_spectrum()
magnitude = np.absolute(hs)
spectrum.hs = magnitude * np.exp(i * angle)

# -- conver spectrum back to a wave with irfft
wave2 = spectrum.make_wave()
wave2.normalize()
segment = wave2.segment(duration=0.005)
# segment.plot()
# plt.xlabel('Time (Hz)')
# plt.savefig('13_sawtooth_inverseplot.png')
# plt.show()

# -- make audio
wave2.make_audio()
# wave.write('06_audio_sawtoot_shuffledphase.wav')
