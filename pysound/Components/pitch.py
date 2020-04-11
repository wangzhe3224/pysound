import numpy as np
from pysound.Models.KS_model import KS


def pitch_gen(freq: float, duration: float, signal: np.array, sample_freq: int, alpha=0.99, ref_length=50):
    """ given a signal, generate a pitch using the signal
    with a frequency (Hz) and duration (Seconds)

    If frequency (f), and sample frequency (f_s) are given, the length of signal is

    desire_signal_length = f_s / f

    Hence if signal length cannot fulfill above, we should either cut or pad the signal.
    """
    total_sample_number = int(sample_freq * duration)
    desire_signal_length = int(sample_freq / freq)
    # pad or cur signal
    if len(signal) >= desire_signal_length:
        input_signal = signal[: desire_signal_length]
    else:  # pad
        input_signal = np.pad(signal, (0, desire_signal_length - len(signal)), 'constant')

    result = KS(input_signal, N=total_sample_number, alpha=alpha, ref_length=ref_length)

    return result


def note_freq(note: str):
    """ Given a note string, return the frequency
    For example:
    D2 -> 73.41619 Hz

    @param note:
    @return:
    """
    # general purpose function to convert a note in standard notation
    # to corresponding frequency
    if len(note) < 2 or len(note) > 3 or \
            note[0] < 'A' or note[0] > 'G':
        return 0
    if len(note) == 3:
        if note[1] == 'b':
            acc = -1
        elif note[1] == '#':
            acc = 1
        else:
            return 0
        octave = int(note[2])
    else:
        acc = 0
        octave = int(note[1])
    SEMITONES = {'A': 0, 'B': 2, 'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2}
    n = 12 * (octave - 4) + SEMITONES[note[0]] + acc
    f = 440 * (2 ** (float(n) / 12.0))
    return f


def freq_note(freq: float) -> str:
    """ Given a frequency, find the closest musical note
    Reference: https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/
    """
    if freq < 0.001:
        return ' '

    A4 = 440
    C0 = A4 * pow(2, -4.75)
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    h = round(12*np.log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[int(n)] + str(int(octave))


def detect_pitch(pitches, magnitudes, t: int):
    """

    @param pitches:
    @param magnitudes:
    @param t: the time index
    @return:
    """
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    return pitch


if __name__ == '__main__':
    f = 440
    f_s = 44000
    dura = 2

    signal = np.random.rand(100)

    output = pitch_gen(f, dura, signal, f_s)
