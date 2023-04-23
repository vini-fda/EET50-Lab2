import numpy as np
from scipy import signal

def dm(x, fs, delta):
    # x = sampled signal to quantize, decode and modulate
    acc = x[0]
    error = []
    accs = [acc]
    ys = []
    dt = 1/fs
    for i in range(len(x)):
        e = x[i] - acc
        y = np.where(e >= 0, 1.0, 0.0)
        error.append(e)
        ys.append(y)
        acc += delta * 2.0 * (ys[i] - 0.5) * dt
        accs.append(acc)
    return np.array(accs)
    #return np.where(np.diff(x, prepend=0) >= 0, 1.0, 0.0)

def dm_sine(f, a, n):
    # n = samples
    # a = amplitude
    # f = frequency
    t = np.linspace(0.0, 1.0, num=n)
    x = a * np.sin(2*np.pi*f*t)
    return dm(x)

def dm_decode(step_size, y):
    y_ = 2*(y - 0.5)
    return np.cumsum(y_) * step_size

def dm_demodulation(x_d, f_c, fs):
    # x_d = decoded signal
    # f_c = cutoff frequency
    # fs = sampling frequency
    # apply scipy's IIR low pass filter to the decoded signal, to obtain the demodulated signal
    b, a = signal.iirfilter(4, f_c, btype='lowpass', fs=fs)
    return signal.filtfilt(b, a, x_d)
