'''Step by step execution of all the examples of DFT'''

from __future__ import print_function, division

import thinkdsp
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt

import numpy as np

import warnings
warnings.filterwarnings('ignore')

PI2 = 2 * np.pi

np.set_printoptions(precision=3, suppress=True)

'''ComplexSinusoid class to calculate the different exponential signals'''
class ComplexSinusoid(thinkdsp.Sinusoid):
     def evaluate(self,ts):
         phases = PI2*self.freq*ts + self.offset
         ys = self.amp * np.exp(1j * phases)
         return ys

signal = ComplexSinusoid(freq = 1, amp = 0.6, offset = 1)
wave = signal.make_wave(duration = 1, framerate = 4)
# np.savetxt('01_complex_sinusoidal_op.txt',wave.ys)

'''Synthesis problem --> Given a set of frequency and amplitude, synthesis the signal'''
# def synthesis1(amps, freqs, ts):
#     components = [thinkdsp.ComplexSinusoid(freq,amp) for amp,freq in zip(amps, freqs)]
#     signal     = thinkdsp.SumSignal(*components)
#     ys         = signal.evaluate(ts)
#     return ys
# 
# amps      = np.array([0.6, 0.25, 0.1, 0.05])
# freqs     = [100, 200, 300, 400]
# framerate = 11025    
# ts        = np.linspace(0,1,framerate)
# ys        = synthesis1(amps, freqs, ts)
# np.savetxt('02_synthesis1.txt',ys)
# n = 500
# thinkplot.plot(ts[:n],ys[:n].real)
# thinkplot.plot(ts[:n],ys[:n].imag)
# plt.savefig('02_Real&Imag.png')
# plt.show()

'''Matrix multiplication --> A better way to implement the previous program'''
def synthesis2(amps, freqs, ts):
    args = np.outer(ts, freqs)
    M    = np.exp(1j*PI2*args)
    ys   = np.dot(M,amps)
    return ys
# 
# amps      = np.array([0.6, 0.25, 0.1, 0.05])
# freqs     = [100, 200, 300, 400]
# framerate = 11025
# ts        = np.linspace(0,1,framerate)
# ys        = synthesis2(amps, freqs, ts)
# np.savetxt('03_synthesis2.txt',ys)
# plt.plot(ts[:500],ys[:500],label=r'$\phi_0 = 0$')
# 
# phi   = 1.5
# amps2 = amps*np.exp(1j*phi)
# ys2   = synthesis2(amps2, freqs, ts)
# np.savetxt('03_synthesis2_phiamp.txt',ys2)
# plt.plot(ts[:500],ys2[:500],label=r'$\phi_0 = 1.5$')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# thinkplot.config(ylim=[-1.15, 1.05], loc='lower right')
# plt.savefig('03_phase_difference_comp.png')
# plt.show()

'''Analysis equation ---> Given freq and samples find the amplitude. x[k]. Linear Algebra approach'''
# def analyze1(ys, freqs, ts):
#     args = np.outer(ts, freqs)
#     M    = np.exp(1j*PI2*args)
#     amps = np.linalg.solve(M, ys)
#     return amps
# 
# n     = len(freqs)
# amps2 = analyze1(ys[:n], freqs, ts[:n])
# np.savetxt('04_analyze1_amps.txt',amps2)

'''Making unitary matrix'''
N      = 4
ts     = np.arange(N)/N
freqs  = np.arange(N)
args   = np.outer(ts, freqs) 
M      = np.exp(1j*PI2*args)
MstarM = M.conj().transpose().dot(M)

def analyze2(ys, freqs, ts):
    args = np.outer(ts, freqs)
    M    = np.exp(1j*PI2*args)
    amps = M.conj().transpose().dot(ys)/N
    return amps

N      = 4
amps = np.array([0.6, 0.25, 0.1, 0.05])
ts     = np.arange(N)/N
freqs  = np.arange(N)
ys = synthesis2(amps, freqs, ts)
amps3 = analyze2(ys, freqs, ts)

'''Making own version of DFT'''
def synthesis_matrix(N):
    ts = np.arange(N)/N
    freqs = np.arange(N)
    args = np.outer(ts, freqs)
    M = np.exp(1j*PI2*args)
    return M
    
def dft(ys):
    N = len(ys)
    M = synthesis_matrix(N)
    amps = M.conj().transpose().dot(ys)
    return amps
    
def idft(ys):
    N = len(ys)
    M = synthesis_matrix(N)
    amps = M.dot(ys)/N
    return amps

# print(ys)    
amps = dft(ys)
# print(amps)
ys = idft(amps)
# print(ys)

'''----------========== REAL SIGNALS ==========----------'''
# framerate = 10000
# signal = thinkdsp.SawtoothSignal(freq = 500)
# wave = signal.make_wave(duration = 0.1, framerate = framerate)
# # wave.plot()
# # plt.xlabel('Time')
# # plt.ylabel('Amplitude')
# # plt.savefig('05_sawtooth_waveform_pic.png')
# # plt.show()
# hs = dft(wave.ys)
# print(len(wave.ys))
# print(len(hs))
# amps = np.absolute(hs)
# # thinkplot.plot(amps)
# # plt.savefig('05_Complete_DFT.png')
# # plt.show()
# 
# N = len(hs)
# fs = np.arange(N)*framerate/N
# thinkplot.plot(fs[:N//2], amps[:N//2])
# plt.savefig('05_proper_freq_DFT.png')
# plt.show()

'''DFT of a real signal is periodic'''
M     = synthesis_matrix(N=8)
np.savetxt('06_dft_real_M_Matrix.txt',M)
Mstar = M.conj().transpose() 
np.savetxt('06_dft_real_Mstar_Matrix.txt',M)

wave = thinkdsp.TriangleSignal(freq = 1).make_wave(duration = 1, framerate = 8)
wave.plot()
plt.xlabel('Time')
plt.ylabel('Amplitude')
# plt.savefig('06_triangular_waveform_pic.png')
# plt.show()

row3 = Mstar[3,:]
row5 = Mstar[5,:]

def approx_equal(a, b, tol=1e-10):
    return sum(abs(a-b)) < tol
    
print(approx_equal(row3, row5.conj()))