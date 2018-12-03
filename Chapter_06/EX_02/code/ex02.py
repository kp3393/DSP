'''Exercise: One of the major applications of the DCT is compression for both sound and images. In its simplest form, DCT-based compression works like this:

Break a long signal into segments.
Compute the DCT of each segment.
Identify frequency components with amplitudes so low they are inaudible, and remove them. Store only the frequencies and amplitudes that remain.
To play back the signal, load the frequencies and amplitudes for each segment and apply the inverse DCT.
Implement a version of this algorithm and apply it to a recording of music or speech. How many components can you eliminate before the difference is perceptible?

thinkdsp provides a class, Dct that is similar to a Spectrum, but which uses DCT instead of FFT.'''

from __future__ import print_function, division

import thinkdsp
import thinkplot
import thinkstats2

import matplotlib.pyplot as plt

import numpy as np
import scipy.fftpack

import warnings
warnings.filterwarnings('ignore')

import timeit
import time

import dct

# -- input a wave
wave = thinkdsp.read_wave('100475__iluppai__saxophone-weep.wav')
wave.make_audio()
# wave.plot()
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.savefig("01_wave")
# plt.show()

# -- Break long signal into segments
segment = wave.segment(start = 1.2, duration = 0.5)
segment.normalize()
segment.make_audio()
# segment.plot()
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.savefig("02_wave_segment")
# plt.show()

# -- Computing DCT of the above segment
seg_dct = segment.make_dct()
seg_dct.plot(high = 4000)
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('DCT')
# plt.savefig("03_wave_segment_dct")
# plt.show()

def remove(dct, thresh):
    count = 0
    for i in range(len(dct.hs)):
        if abs(dct.hs[i])<thresh:
            dct.hs[i]=0
            count +=1
    n = len(dct.hs)
    percent = (count/n)*100
    print(count,n,percent,sep='\t')

remove(seg_dct, thresh = 10)
seg_dct.plot(high = 4000)
plt.xlabel('Frequency (Hz)')
plt.ylabel('DCT')
plt.savefig("04_wave_segment_reduced_dct")
plt.show()
