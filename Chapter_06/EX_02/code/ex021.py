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
print(len(wave.ys))

# -- make spectrogram for segments
def make_dct_spectogram(wave, seg_length):
    window = np.hamming(seg_length)
    i = 0
    j = seg_length
    step = seg_length//2
    spec_map = {}

    while j<len(wave.ys):
        segment = wave.slice(i,j)
        segment.window(window)

        t = (segment.start + segment.end)/2
        spec_map[t] = segment.make_dct()

        i += step
        j += step

    return thinkdsp.Spectrogram(spec_map, seg_length)

def remove(dct, thresh):
    count = 0
    for i in range(len(dct.hs)):
        if abs(dct.hs[i])<thresh:
            dct.hs[i]=0
            count +=1
    n = len(dct.hs)
    percent = (count/n)*100
    print(count,n,percent,sep='\t')

spectro = make_dct_spectogram(wave, seg_length = 1024)
for t,dct in sorted(spectro.spec_map.items()):
    remove(dct,thresh = 0.2)
