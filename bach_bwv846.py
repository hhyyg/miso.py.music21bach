#%%
from music21 import note,stream,corpus,chord,environment,converter,midi

#%%
bwv846 = corpus.parse('bach/bwv846')
bwv846.measures(1, 2).show()

#%%
bwv846.show('midi')

#%%
bwv846.parts[0].plot()
bwv846.parts[1].plot()

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
f = bwv846.parts[0].flat
note16count = [note for note in f.notes if note.quarterLength == 0.25]
len(note16count)