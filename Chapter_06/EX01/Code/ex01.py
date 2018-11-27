'''Exercise 6.1 In this chapter I claim that analyze1 takes time proportional
to n3 and analyze2 takes time proportional to n2. To see if that’s true, run
them on a range of input sizes and time them. In Jupyter, you can use the
“magic command” %timeit.
If you plot run time versus input size on a log-log scale, you should get a
straight line with slope 3 for analyze1 and slope 2 for analyze2.
You also might want to test dct_iv and scipy.fftpack.dct.'''

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

#Let us create a signal to play with with random numbers
signal = thinkdsp.UncorrelatedGaussianNoise()
noise  = signal.make_wave(duration = 1.0, framerate = 16384)
noise.ys.shape
ns = 2**np.arange(6,15)

#defining a function which takes an array of results from a timing experiment, plots a result and fits a straight line.
def plot_bests(bests):
    thinkplot.plot(ns, bests)
    thinkplot.config(xscale='log', yscale='log', legend=False)
    x = np.log(ns)
    y = np.log(bests)
    t = scipy.stats.linregress(x,y)
    slope = t[0]
    plt.show()
    plt.savefig("01_analyze1_time")
    print(slope)

    return slope

# results = []
# for N in ns:
#     print(N)
#     ts = (0.5+np.arange(N))/N
#     freqs = (0.5+np.arange(N))/2
#     ys = noise.ys[:N]
#     mysetup = '''
# from __main__ import ts, freqs, ys, dct
# import dct'''
#
#     mycode = '''dct.analyze1(ys, freqs, ts)'''
#     result = timeit.repeat(setup = mysetup, stmt = mycode,repeat = 3, number = 5)
#     results.append(min(result))
#
# plot_bests(results)

results = []
for N in ns:
    print(N)
    ts = (0.5 + np.arange(N)) / N
    freqs = (0.5 + np.arange(N)) / 2
    ys = noise.ys[:N]
    mysetup = '''
from __main__ import ts, freqs, ys, dct
import dct'''
    mycode = '''dct.analyze1(ys, freqs, ts)'''
    result =  timeit.repeat(setup = mysetup, stmt = mycode,repeat = 3, number = 5)
    results.append(min(result))

plot_bests(results)


# -- PROGRAM EXECUTIONS TAKE REALLY LONG TIME SO COULD NOT FINISH THE WHOLE EXECUTION. -- #
