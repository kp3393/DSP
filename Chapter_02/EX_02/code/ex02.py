# -- Exercise 2.2 A sawtooth signal has a waveform that ramps up linearly from
# -- -1 to 1, then drops to -1 and repeats. See http://en.wikipedia.org/wiki/
# -- Sawtooth_wave
# -- Write a class called SawtoothSignal that extends Signal and provides
# -- evaluate to evaluate a sawtooth signal.
# -- Compute the spectrum of a sawtooth wave. How does the harmonic structure
# -- compare to triangle and square waves?

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

# -- Write a class called SawtoothSignal that extends Signal
# -- Since the class inherits the parent class of signals. It inerits the __init__ nethod from it.
# -- Thus taking the same arguments: freq, amp, offset.
class SawtoothSignal(thinkdsp.Sinusoid):
    # -- provides evaluate to evaluate a sawtooth signal.
    def evaluate(self, ts):
        cycles = self.freq*ts + self.offset/PI2
        # with open("cycles.txt","w") as fhandle:
        #     for i in range(len(cycles)):
        #         output = str(cycles[i])+"\n"
        #         fhandle.write(output)
        frac,_ =np.modf(cycles)
        # with open("frac.txt","w") as fhandle:
        #     for i in range(len(frac)):
        #         output = str(frac[i])+"\n"
        #         fhandle.write(output)
        ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
        return ys


# -- make sawtooth waveform
sawtooth = SawtoothSignal().make_wave(duration = 0.5, framerate = 40000)
sawtooth.make_audio()
# sawtooth.write("01_sawtooth.wav")

# -- plot the sawtooth spectrum
# sawtooth.make_spectrum().plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('02_sawtooth_spectrum.png')
# plt.show()

# -- compare it with the square wave.
# sawtooth.make_spectrum().plot(color = 'gray')
# square = thinkdsp.SquareSignal().make_wave(duration = 0.5, framerate = 40000)
# square.make_spectrum().plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('03_comparison_same_amp.png')
# plt.show()

# sawtooth.make_spectrum().plot(color = 'gray')
# square = thinkdsp.SquareSignal(amp = 0.5).make_wave(duration = 0.5, framerate = 40000)
# square.make_spectrum().plot()
# plt.xlabel('Frequency (Hz)')
# plt.savefig('04_comparison_squareamp_reduced.png')
# plt.show()

# -- comparison with triangular wave.
sawtooth.make_spectrum().plot(color = 'gray')
triangle = thinkdsp.TriangleSignal(amp = 0.79).make_wave(duration = 0.5, framerate = 40000)
triangle.make_spectrum().plot()
plt.xlabel('Frequency (Hz)')
plt.savefig('05_comparison_triangle_sawtooth.png')
plt.show()
