import numpy as np
from pysound.Models.KS_model import KS
from pysound.Components.pitch import note_freq


def ks_chord(chord, N, alpha, f_s):
    """
    Generate a chord using random signal. The idea is aggregate different pitches
    @param chord:
        hdn_chord = {
                'D2' : 2.2,
                'D3' : 3.0,
                'F3' : 1.0,
                'G3' : 3.2,
                'F4' : 1.0,
                'A4' : 1.0,
                'C5' : 1.0,
                'G5' : 3.5,
            }
    @param N:
    @param alpha:
    @param f_s:
    @return:
    """
    y = np.zeros(N)
    # the chord is a dictionary: pitch => gain
    for note, gain in chord.items():
        # create an initial random-filled KS buffer the note
        x = np.random.randn(int(np.round(float(f_s) / note_freq(note))))
        y = y + gain * KS(x, N, alpha)
    return y
