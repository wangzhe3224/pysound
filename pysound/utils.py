import numpy as np

from pysound.Components.pitch import note_freq


def check_board(size: int):
    """ Generate grey scale checkboard
    plt.gray()
    @param size: the size of check board
    @return:
    """
    img = np.zeros((size, size))
    for n in np.arange(0, size):
        for m in np.arange(0, size):
            if (n & 0x01) ^ (m & 0x01):
                img[n, m] = 255  # black
    # plt.matshow(img)
    return img


def play_notes(melody, time_scale=1.0, rate=32000, wave_engine=None):
    """ play note in melody list
    tune = (('B4', 2), ('B5', 2), ('F#5', 2), ('D#5', 2), ('B5', 1), ('F#5', 3), ('D#5', 4),
            ('C5', 2), ('C6', 2), ('G5', 2),  ('E5', 2),  ('C6', 1), ('G5', 3),  ('E5', 4),
            ('B4', 2), ('B5', 2), ('F#5', 2), ('D#5', 2), ('B5', 1), ('F#5', 3), ('D#5', 4),
            ('D#5', 1), ('E5', 1), ('F5', 2), ('F5', 1), ('F#5', 1), ('G5', 2), ('G5', 1),
            ('G#5', 1), ('A5', 2), ('B5', 4))

    SF = 24000
    jingle = play_notes(tune, time_scale=0.06, rate=SF)
    IPython.display.Audio(jingle, rate=SF)

    We can have more fun!!

    tune_bass = (('B2', 6), ('B3', 2), ('B2', 6), ('B3', 2), ('C3', 6), ('C4', 2), ('C3', 6), ('C4', 2),
             ('B2', 6), ('B3', 2), ('B2', 6), ('B3', 2),
             ('F#3', 4), ('G#3', 4), ('A#3', 4), ('B3', 4))

    SF = 24000
    pacman = jingle + play_notes(tune_bass, time_scale=0.06, rate=SF)
    IPython.display.Audio(pacman, rate=SF)

    @param melody:
    @param time_scale:
    @param rate:
    @param wave_engine:
    @return:
    """
    # melody is a tuple of pairs, each pair containing the pitch and the duration
    #  of each note; time_scale gives the base length of a note of unit duration
    if not wave_engine:
        raise ValueError('Must provide a wave generating function in wave_engine.')
    s = []
    for note in melody:
        f = 2 * np.pi * note_freq(note[0]) / float(rate)
        #
        N = int(note[1] * rate * time_scale)
        if f > 0:
            s = np.concatenate((s, wave_engine(f, N)))
        else:
            s = np.concatenate((s, np.ones(N)))
    return s


if __name__ == '__main__':
    from pysound.Components.waves import square_wave_exact
    import IPython

    bdbm_1 = (('Bb4', 4), ('Eb5', 6), ('F5', 2), ('D5', 8), (' ', 4),
              ('Eb5', 4), ('Ab4', 4), ('Ab4', 4), ('Ab4', 8), ('G4', 4),
              (' ', 2), ('Bb4', 2), ('D5', 2), ('Bb4', 2), ('A4', 2), ('Bb4', 2),
              ('F4', 2), ('Bb4', 2), ('D5', 2), ('Bb4', 2), ('A4', 2), ('Bb4', 2),
              ('Eb4', 4), ('C5', 6), ('D5', 1), ('Eb5', 1),
              ('D5', 3), ('C5', 1), ('Bb4', 3), ('C5', 1), ('F4', 3), ('A4', 1),
              ('Bb4', 12),)

    bdbm_2 = (('G4', 4), ('G4', 4), ('A4', 4), ('Bb4', 8), (' ', 4), ('Bb4', 4),
              ('F4', 4), ('F4', 4), ('F4', 8), (' ', 4), ('G4', 12), ('F4', 12),
              (' ', 12), (' ', 8), ('Eb4', 4), (' ', 12),)

    bdbm_3 = ((' ', 12), ('F4', 8), (' ', 4), ('Eb4', 4), ('F4', 4), ('C3', 4),
              ('Bb3', 4), ('D4', 4), ('Eb4', 4), (' ', 12), ('D4', 12), ('Bb3', 4),
              ('F4', 4), ('A4', 4), ('Bb4', 4), ('G4', 4), ('Eb4', 4), ('D4', 12),)

    bdbm_4 = (('Eb3', 4), ('C3', 4), ('F3', 4), ('Bb2', 4), ('Bb3', 4), ('Ab3', 4),
              ('G3', 4), ('F3', 4), ('Eb3', 4), ('D3', 4), ('Bb2', 4), ('Eb2', 4),
              ('E2', 4), ('E2', 4), ('E2', 4), ('F2', 4), ('F2', 4), ('F2', 4),
              ('G2', 4), ('A2', 4), ('F2', 4), ('Bb2', 4), ('Eb2', 4), ('F2', 4), ('Bb2', 12),)

    SF = 24000
    s =  play_notes(bdbm_1, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_2, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_3, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_4, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)

    IPython.display.Audio(s, rate=SF)