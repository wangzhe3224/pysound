from pysound.Components.pitch import note_freq, freq_note, detect_pitch
from pysound.Components.waves import *
from librosa.core.pitch import *
from pysound.utils import play_notes


def test_freq_note():

    freq = 440*2
    note = freq_note(freq)
    assert note == 'A5'

    freq = 440 * 2 * 1.4
    note = freq_note(freq)
    assert note == 'D#6'


def test_pitch_detect():
    # Generate melody
    bdbm_1 = (('Bb4', 4),)

    SF = 24000  # sample rate
    s = play_notes(bdbm_1, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)

    # detect pitch
    pitches, magnitute = piptrack(y=s, sr=SF)
    p = detect_pitch(pitches, magnitute, t=4)
    assert freq_note(p) == 'A#4'
