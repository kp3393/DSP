'''Exercise 5.2 The example code in chap05.ipynb shows how to use autocorrelation
to estimate the fundamental frequency of a periodic signal. Encapsulate
this code in a function called estimate_fundamental, and use it to
track the pitch of a recorded sound.
To see how well it works, try superimposing your pitch estimates on a spectrogram
of the recording.'''

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

def serial_corr(wave, lag=1):
    N = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:N-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr

def autocorr(wave):
    lags = range(len(wave.ys)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

def estimate_fundamental(wave, start, duration):
    wave.normalize()
    segment = wave.segment(start = start, duration = duration)
    lags, corrs = autocorr(segment)
    thinkplot.plot(lags, corrs)
    plt.xlabel('Lag(Index)')
    plt.ylabel('Correlation')
    plt.savefig('05_Segment_Autocorr.png')
    plt.show()
    lag = np.argmax(corrs[1:])+1
    frequency = (segment.framerate)/((lag))
    print(lag)
    print(frequency)
    #print(corrmax)

wave = thinkdsp.read_wave('28042__bcjordan__voicedownbew.wav')
est = estimate_fundamental(wave, 0.2, 0.01)
