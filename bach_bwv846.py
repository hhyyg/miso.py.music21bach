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
right16notes = [note for note in f.notes if note.quarterLength == 0.25]
len(right16notes)

#%%
bwv846 = corpus.parse('bach/bwv846')
bwv846chord = stream.Stream()

for measure_number in range(1, 36):
    new_notes = []
    target_measure = bwv846.measures(measure_number, measure_number)
    m_notes = target_measure.flat.notes

    for n in m_notes:
        n.offset = 0
        # new_note = note.Note(pitchName=n.pitchName)
        # new_note.duration = duration.Duration(1)
        # new_notes.append(new_note)
    
    # re = chord.Chord(new_notes)
    # bwv846chord.append(re)