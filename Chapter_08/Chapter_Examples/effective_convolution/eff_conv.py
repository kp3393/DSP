from __future__ import print_function, division
import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import scipy.signal
import matplotlib.pyplot as plt



names = ['date', 'open', 'high', 'low', 'close', 'volume']
df = pd.read_csv('fb.csv', header=0, names=names)
ys = df.close.values[::-1]
dates = df.date.values[::-1]
plt.plot(dates,ys,color = 'black')
N=len(ys)

window = scipy.signal.gaussian(M=30, std = 6)
window /= sum(window)

padded = thinkdsp.zero_pad(window,N)

smoothed = np.convolve(ys, window, mode = 'valid')

# plt.plot(dates,smoothed,color = 'red')

# plt.plot()
# plt.show()
def fft_conv(signal,window):
    fft_signal = np.fft.rfft(signal)
    fft_window = np.fft.rfft(window)
    return np.fft.ifft(fft_signal*fft_window)

smooth2 = fft_conv(ys,padded)
# plt.plot(dates,smooth2,color = 'purple')


