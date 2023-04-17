import numpy as np
from scipy import signal

def pcm(x, a, k):
    # x = sampled signal to quantize
    # a = amplitude
    # k = bits  
    return pcm_modulation(pcm_codification(pcm_quantization(x, a, k), k))

def pcm_quantization(x, a, k):
    # x = sampled signal to quantize
    # a = amplitude
    # k = bits
    return np.round(0.5 * (1 + x/a) * (2**k - 1))

def pcm_codification(ns, k):
    fstr = "{0:0" + f'{k}b' + "}"
    fmt = lambda n: fstr.format(int(n))
    return np.array(list(map(fmt, ns)))

def pcm_modulation(x_c):
    str_numbers = ''.join(x_c)
    return np.array(list(map(int, str_numbers)))

def pcm_sine(f, a, k, n):
    # n = samples
    # a = amplitude
    # f = frequency
    # k = bits
    t = np.linspace(0.0, 1.0, num=n)
    x = a * np.sin(2*np.pi*f*t)
    return pcm(x, a, k)

def pcm_inv(f_c, f_s, y, a, k):
    return pcm_demodulation(pcm_decodification(y, a, k), f_c, f_s)

def pcm_decodification(y, a, k):
    # y = binary encoded signal
    # a = amplitude
    # k = bits
    delta = a / 2**(k-1)
    f = lambda x: int(x, 2) * delta - a + delta/2
    return np.array(list(map(f, y)))

def pcm_demodulation(x_d, f_c, fs):
    # x_d = decoded signal
    # f_c = cutoff frequency
    # fs = sampling frequency
    # apply scipy's IIR low pass filter to the decoded signal60.0, to obtain the demodulated signal
    b, a = signal.iirfilter(4, f_c, btype='lowpass', fs=fs)
    return signal.filtfilt(b, a, x_d)
