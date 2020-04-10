import scipy.signal as sp


def freq_extract(freq: float, signal, sf, N:int=6):
    """ Extract some frequency from the signal using butter filter

    @param freq:
    @param signal:
    @param N: the degree of butter filter
    @param sf:
    @return:
    """
    wc = freq / (sf/2)
    b, a = sp.butter(N, wc)
    y = sp.lfilter(b, a, signal)
    return y
