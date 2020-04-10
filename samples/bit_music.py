from pysound.Components.waves import square_wave_exact
from pysound.utils import play_notes
from scipy.io.wavfile import write
import IPython

if __name__ == '__main__':
    """ generate bit music from notes """
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

    SF = 24000  # sample rate
    s = play_notes(bdbm_1, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_2, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_3, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)
    s += play_notes(bdbm_4, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)

    IPython.display.Audio(s, rate=SF)
    write('./test.wav', SF, s)