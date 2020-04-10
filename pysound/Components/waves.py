import numpy as np


def square_wave(w, N):
    """ Generate sauare wave

    @param w: radints
    @param N: samples
    @return:
    """
    p = np.round(2 * np.pi / w)
    return np.where((np.arange(0, N) % p) >= (p/2), -1, 1)


def square_wave_exact(w, N):
    """ need more computation but more prise """
    return np.where(np.sin(np.arange(0, N) * w) >= 0, 1, -1)
