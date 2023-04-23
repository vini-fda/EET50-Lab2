import pcm
import dm
import numpy as np
import matplotlib.pyplot as plt

def pcm_plot(t_min, t_max, x, a, k):
    # x = sampled signal to quantize
    # a = amplitude
    # k = bits
    x_q = pcm.pcm(x, a, k)
    # hold each pulse for the sampling period T
    n = len(x_q)
    # must be rectangle plot
    #plt.stem(np.arange(n), x_q, 'k', markerfmt='ko', use_line_collection=True)
    # plot rectangular pulses
    t = np.linspace(t_min, t_max, n)
    plt.step(t, x_q, 'k')
    # x title
    #plt.xlabel(r'Índice da amostra $n \propto t$')
    plt.xlabel(r'Tempo $t$ [s]')

def dm_plot(t_min, t_max, x, fs, n, step_size):
    # x = sampled signal to quantize
    # a = amplitude
    # k = bits
    x_new = x[::n]
    x_q = dm.dm(x_new, fs / n, step_size)
    new_fs = fs / n
    x_demod = dm.dm_demodulation(x_q, new_fs / 3.0, new_fs)
    # hold each pulse for the sampling period T
    n = len(x_q)
    # must be rectangle plot
    #plt.stem(np.arange(n), x_q, 'k', markerfmt='ko', use_line_collection=True)
    # plot rectangular pulses
    t = np.linspace(t_min, t_max, n)
    plt.step(t, x_q, 'k', label=r'Quantizado $\hat{x}(t)$')
    plt.plot(t, x_demod, color='orange', linestyle='-', label=r'Demodulado $\bar{x}(t)$')
    plt.legend()
    # x title
    #plt.xlabel(r'Índice da amostra $n \propto t$')
    plt.title(r'Modulação DM de $x(t)$')
    plt.xlabel(r'Tempo $t$ [s]')