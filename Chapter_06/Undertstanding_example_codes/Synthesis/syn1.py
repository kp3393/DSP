from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy as np

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

PI2 = np.pi * 2

def synthesize1(amps, fs, ts):
    components = [thinkdsp.CosSignal(freq, amp) for amp, freq in zip(amps, fs)] 
    signal = thinkdsp.SumSignal(*components)

    ys = signal.evaluate(ts)
    return ys

amps = np.array([0.6, 0.25, 0.1, 0.05])
fs = [100, 200, 300, 400]
framerate = 11025

ts = np.linspace(0, 1, framerate)
ys = synthesize1(amps, fs, ts)
wave = thinkdsp.Wave(ys, ts, framerate)
wave.apodize()
wave.make_audio()
