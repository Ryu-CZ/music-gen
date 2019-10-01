from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
base_time = 8

track.append(Message('program_change', program=12, time=0))
track.append(Message('aftertouch', value=127, time=0))


track.append(Message('note_off', note=64, velocity=127, time=base_time*10))
for i in range(1, 8):
    duration = base_time * (2**i)
    track.append(Message('note_on', note=64, velocity=96, time=duration))
    track.append(Message('note_off', note=64, velocity=127, time=duration))
    track.append(Message('aftertouch', value=int(127 / i), time=0))
track.append(Message('note_off', note=64, velocity=127, time=base_time*10))


mid.save('./tracks/new_song.mid')
