'''Exercise: A Geiger counter is a device that detects radiation. When an ionizing particle strikes the detector, it outputs a surge of current.
The total output at a point in time can be modeled as uncorrelated Poisson (UP) noise, where each sample is a random quantity from a Poisson distribution,
which corresponds to the number of particles detected during an interval.
Write a class called UncorrelatedPoissonNoise that inherits from thinkdsp._Noise and provides evaluate.
It should use np.random.poisson to generate random values from a Poisson distribution.
The parameter of this function, lam, is the average number of particles during each interval.
You can use the attribute amp to specify lam. For example, if the framerate is 10 kHz and amp is 0.001, we expect about 10 “clicks” per second.
Generate about a second of UP noise and listen to it. For low values of amp, like 0.001, it should sound like a Geiger counter.
For higher values it should sound like white noise. Compute and plot the power spectrum to see whether it looks like white noise. '''

from __future__ import print_function, division

import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

""" Personal comments about understanding of the problem.
So the Geiger counter output is modeled as uncorrelated poisson noise.
Each sample is a RANDOM QUANTITY from POISSON DISRIBUTION.
The task is to write a class called UncorrelatedPoissonNoise which helps in generating random values from POISSON DISRIBUTION.
How to create this random samples?
np.random.poisson(lam, size) --> where lam is the expectation of the interval.
So if we have amp of 0.001 with a framerate of 10KHz i.e for each interval we expect 0.001 thus in the whole interval of 1 sec it would be duration*framerate*amp
thus 1*10000*0.001 which is 10 clicks per second
 """

class UncorrelatedPoissonNoise(thinkdsp._Noise):
    '''Represents the class UncorrelatedPoissonNoise which inherits thinkdsp._Noise'''
    def evaluate(self, ts):
        ys = np.random.poisson(self.amp, len(ts))
        return ys

amp = 0.001
framerate = 10000
duration = 1

signal = UncorrelatedPoissonNoise(amp=amp)
wave = signal.make_wave(duration=duration, framerate=framerate)
wave.make_audio()
wave.write('01_Geiger_Counter.wav')

"Verifying the result."
expected = amp*framerate*duration
actual = sum(wave.ys)
print(expected, actual)

"Plotting the results"
# wave.plot()
# plt.xlabel("Time (Sec)")
# plt.ylabel("Amplitude")
# plt.savefig("01_Gerger_Counter_Wave")
# plt.show()

"Plotting power spectrum"
# spectrum = wave.make_spectrum()
# spectrum.plot_power()
# plt.loglog()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Power")
# plt.savefig("01_Gerger_Counter_Power_Spectrum")
# plt.show()
# print(spectrum.estimate_slope().slope

"Higher arrival sound it looks like white noise"
amp = 1
duration = 1
framerate = 10000

signal = UncorrelatedPoissonNoise(amp=amp)
wave = signal.make_wave(duration=duration, framerate=framerate)
wave.make_audio()
# wave.write("02_Geiger_counter_high_amp.wav")

"Plotting the results"
# wave.plot()
# plt.xlabel("Time (Sec)")
# plt.ylabel("Amplitude")
# plt.savefig("02_Geiger_counter_high_amp")
# plt.show()

"Plotting power spectrum"
spectrum = wave.make_spectrum()
spectrum.plot_power()
plt.loglog()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.savefig("02_Gerger_Counter_highamp_Power_Spectrum")
plt.show()
print(spectrum.estimate_slope().slope)
