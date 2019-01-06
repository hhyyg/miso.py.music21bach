# https://github.com/cuthbertLab/music21/blob/master/music21/serial.py

#%%
from music21 import serial,note,stream,corpus,chord,environment,converter,midi

ttr = serial.TwelveToneRow([0, 2, 11, 7, 8, 3, 9, 1, 4, 10, 5, 6])
aMatrix = ttr.matrix()
print(aMatrix)

#%%
ttr.show()

#%% 
ttr.getIntervalsAsString()

#%%
ttr.noteNames()

#%%
bStream = stream.Stream()
for i in range(0, 12, 3):
    c = chord.Chord(ttr[i:i + 3])
    c.addLyric(c.primeFormString)
    c.addLyric(c.forteClass)
    bStream.append(c)
bStream.show()

#%%
bStream.show('midi')

#%%
line = [5*i for i in range(12)]
r = serial.pcToToneRow(line)
r.noteNames()

#%%
r.isTwelveToneRow()

#%%
r.getIntervalsAsString()

#%%
invalid_l = [6*i for i in range(12)]
invalid_r = serial.pcToToneRow(invalid_l)
invalid_r.noteNames()

#%% 
invalid_r.isTwelveToneRow()
