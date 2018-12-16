#%%
from music21 import note,stream,corpus,chord,environment,converter,midi

#%%
stream1 = stream.Stream()

note = note.Note("C4", quarterLength = 1)
stream1.repeatAppend(note, 4)
stream1.show()

#%%
stream1.show('midi')

#%% 
s = converter.parse('tinyNotation: 4/4 e8 e8 r e8 r c8 e8 r g4 r G4 r')
s.show()




