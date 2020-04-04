import numpy as np


def KS(x, N, alpha=0.99, ref_length: int = 50):
    """ Karplus-Strong Algorithm is a simple digital feedback loop with an 
    internal buffer of  MM  samples. The buffer is filled with a set of initial values 
    and the loop, when running, produces an arbitraryly long output signal

    :param x: array of ints
    :param N: length of produced samples
    :param ref_length: decay buffer length
    """
    M = len(x)
    a = alpha ** (float(M) / ref_length)
    y = np.zeros(N)

    for n in np.arange(0, N):
        y[n] = (x[n] if n < M else 0) + a * (y[n - M] if n - M > 0 else 0)

    return y
