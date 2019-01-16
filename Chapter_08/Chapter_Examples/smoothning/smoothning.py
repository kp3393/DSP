from __future__ import print_function, division
import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import scipy.signal
import matplotlib.pyplot as plt

np.set_printoptions(precision=3, suppress=True)
PI2 = 2 * np.pi
GRAY = '0.7'

'''SMOOTHING'''
def smooth(n,segment):
    window = np.ones(n)                                                         # create a window of ones for the given window size
    window /=sum(window)                                                        # Normalise it. 

    ys = segment.ys                                                             # get the y values of the samples.
    N = len(ys)                                                                 # N is length of ys.
    padded = thinkdsp.zero_pad(window,N)                                        # Since the window size and the sample size are different we need to do zerom padding so that multiplication is possible.
    smoothed = np.zeros(N)                                                      # smoothed is list which will consist of all the smoothened values.

    for i in range(N):
        smoothed[i] = sum(padded * ys)
        padded = np.roll(padded,1)
    return smoothed

signal = thinkdsp.SquareSignal(freq=440)
wave = signal.make_wave(duration=1, framerate=44100)
segment = wave.segment(duration=0.01)

plt.plot(segment.ts,segment.ys,color='blue')

n = input('Enter the window size:')
n = int(n)

ys2 = smooth(n,segment)
plt.plot(segment.ts,ys2,color='grey')
plt.show()
plt.savefig('01_squarewave.png')

        
        

    
