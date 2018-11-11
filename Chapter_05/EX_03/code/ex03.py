'''Exercise 5.3 If you did the exercises in the previous chapter, you downloaded
the historical price of BitCoins and estimated the power spectrum
of the price changes. Using the same data, compute the autocorrelation of
BitCoin prices. Does the autocorrelation function drop off quickly? Is there
evidence of periodic behavior?'''
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

def autocorr(wave):
    lags = range(len(wave.ys)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs

def serial_corr(wave, lag=1):
    N = len(wave)
    y1 = wave.ys[lag:]
    y2 = wave.ys[:N-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr

df = pd.read_csv('coindesk-bpi-USD-close_data-2017-10-28_2018-10-28.csv', nrows=366, parse_dates=[0])
ys = df['Close Price']
ts = np.arange(len(ys))
wave = thinkdsp.Wave(ys, ts, framerate=1)

# wave.plot()
# plt.xlabel("Time (Days)")
# plt.ylabel("Close Price")
# plt.savefig("01 Bitcoin prices for one year (2017-10-28_2018-10-28)")
# plt.show()

lags, corrs = autocorr(wave)
thinkplot.plot(lags, corrs, color = 'red')
# plt.xlabel('Lag(Index)')
# plt.ylabel('Correlation')
# plt.savefig('02_Bitcoin_Correlation.png')
# plt.show()

'''No there is no evidence of periodic behaviour'''

''' Comparison between autocorr and np.correlate'''

N = len(wave)
corrs2 = np.correlate(wave.ys,wave.ys,mode = 'same')
lags = np.arange(-N//2,N//2)
# thinkplot.plot(lags, corrs2)
# plt.xlabel('Lag(Index)')
# plt.ylabel('Dot product')
# plt.savefig('03_comparison.png')
# plt.show()

N = len(corrs2)
half = corrs2[N//2:]
# thinkplot.plot(half)
# plt.xlabel('Lag(Index)')
# plt.ylabel('Dot product')
# plt.savefig('04_comparison_half.png')
# plt.show()

lengths = range(N, N//2, -1)
half /= lengths
half /= half[0]
thinkplot.plot(half)
plt.xlabel('Lag(Index)')
plt.ylabel('Dot product')
plt.savefig('06_comparison_autocarr_correlation.png')
plt.show()
