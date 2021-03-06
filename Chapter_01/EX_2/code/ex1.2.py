# -- Exercise 1.2 Go to http://freesound.org and download a sound sample
# -- that includes music, speech, or other sounds that have a well-defined pitch.
# -- Select a roughly half-second segment where the pitch is constant. Compute
# -- and plot the spectrum of the segment you selected. What connection can
# -- you make between the timbre of the sound and the harmonic structure you
# -- see in the spectrum?

# -- for the sake of verification of results two samples will be analysed.
# -- One which is there in solution and other a random one.

from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from IPython.html.widgets import interact, fixed
from IPython.display import display

# -- wave selection
wave = thinkdsp.read_wave('170255__dublie__trumpet.wav')
wave.normalize()
# wave.make_audio()
wave.plot()
plt.xlabel('Time (s)')
plt.savefig('01_trumpet.png')
plt.show()

# -- segment selection
segment = wave.segment(start=1.1, duration=0.3)
segment.plot()
plt.xlabel('Time (s)')
plt.savefig('02_trumpet_segment.png')
plt.show()

# -- spectrum plot
spectrum = segment.make_spectrum()
spectrum.plot(high = 7000)
plt.xlabel('Frequency (Hz)')
plt.savefig('03_trumpet_spectrum.png')
plt.show()

# -- shorter segment selection
segment.segment(start=1.1, duration=0.005)
segment.plot()
plt.xlabel('Time (s)')
plt.savefig('02_trumpet_short_segment.png')
plt.show()

# -- shorter segment spectrum plot
spectrum = segment.make_spectrum()
spectrum.plot(high = 1000)
plt.xlabel('Frequency (Hz)')
plt.savefig('03_trumpet_short_spectrum.png')
plt.show()

# -- prints the highest points in the spectrum and their frequencies, in descending order:
print(spectrum.peaks()[:30])

# -- Applying filters. 3400Hz to hear the audio file at low frequencies
wave_spec = wave.make_spectrum()
wave_spec.low_pass(3400)
wave_spec.plot()
plt.xlabel('Frequency (Hz)')
plt.savefig('05_trumpet_spectrum.png')
plt.show()
filtered = wave_spec.make_wave()
filtered.normalize()
filtered.apodize()
filtered.write("Trumpet_LPF.wav")
