# Exercise: At http://www.coindesk.com you can download the daily price of a BitCoin as a CSV file.
# Read this file and compute the spectrum of BitCoin prices as a function of time. Does it resemble white, pink, or Brownian noise?
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

df = pd.read_csv('coindesk-bpi-USD-close_data-2017-10-28_2018-10-28.csv', nrows=366, parse_dates=[0])
#ys = df.Close.values
ys = df['Close Price']
ts = np.arange(len(ys))
wave = thinkdsp.Wave(ys, ts, framerate=1)

# wave.plot()
# plt.xlabel("Time (Days)")
# plt.ylabel("Close Price")
# plt.savefig("01 Bitcoin prices for one year (2017-10-28_2018-10-28)")
# plt.show()

spect = wave.make_spectrum()
# spect.plot()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.savefig("02 Bitcoin prices for one year (2017-10-28_2018-10-28)_spectrum.png")
# plt.show()

spect.plot_power()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Power")
# plt.loglog()
# plt.savefig("03 Bitcoin prices for one year (2017-10-28_2018-10-28)_PSD.png")
# plt.show()

print(spect.estimate_slope()[0])                                                # Slope is -1.8851685913744234
