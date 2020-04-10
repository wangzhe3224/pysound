from pysound.Components.pitch import note_freq, freq_note


def test_freq_note():

    freq = 440*2
    note = freq_note(freq)
    assert note == 'A5'