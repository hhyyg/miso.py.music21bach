#%%
from music21 import note,stream,corpus,chord,environment,converter,midi,duration,chord
import matplotlib as pyplot
pyplot.rcParams['figure.figsize'] = (20.0, 10.0)
pyplot.rcParams["figure.dpi"] = 200

#%%
bachCount = corpus.getComposer('bach')
len(bachCount)

#%%
bwv846 = corpus.parse('bach/bwv846')
bwv846.measures(1, 2).show()

#%%
bwv846.show('midi')

#%%
bwv846.parts[0].plot()
bwv846.parts[1].plot()
bwv846.plot()

#%%
bwv846.plot('histogram', 'pitch')

#%%
bwv846.plot('histogram', 'pitchClass')

#%%
bwv846.plot('3dbars', 'pitchClass')

#%%
bwv846.parts[0].plot('histogram', 'quarterLength', title='right hand')
bwv846.parts[1].plot('histogram', 'quarterLength', title='left hand')

#%%
bwv846.measures(11, 16).show()

#%%
f = bwv846.parts[0].flat
note16count = [note for note in f.notes if note.quarterLength == 0.25]
len(note16count)

#%%
bwv846 = corpus.parse('bach/bwv846')
bwv846chord = stream.Stream()
for measure_number in range(1, 36):
    new_notes = []
    for n in bwv846.measures(measure_number, measure_number + 1).notes:
        print(n.pitchName)
        # new_note = note.Note(pitchName=n.pitchName)
        # new_note.duration = duration.Duration(1)
        # new_notes.append(new_note)
    
    # re = chord.Chord(new_notes)
    # bwv846chord.append(re)

# bwv846chord.show()
