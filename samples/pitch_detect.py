from librosa.core.pitch import piptrack

from pysound.Components.pitch import detect_pitch, freq_note
from pysound.Components.waves import square_wave_exact
from pysound.utils import play_notes

# Generate melody
bdbm_1 = (('Bb4', 4), )

SF = 24000  # sample rate
s = play_notes(bdbm_1, time_scale=0.2, rate=SF, wave_engine=square_wave_exact)

# detect pitch
pitches, magnitute = piptrack(y=s, sr=SF)

t = 0
for t in range(pitches.shape[1]):
    p = detect_pitch(pitches, magnitute, t=t)
    print('Pitch at {} is {}'.format(t, freq_note(p)))