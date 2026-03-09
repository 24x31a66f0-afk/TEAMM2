from midiutil import MIDIFile
import random

def generate_music(emotion, duration):

    midi = MIDIFile(1)

    track = 0
    time = 0

    if emotion == "joy":

        tempo = 140
        notes = [72,76,79,84]

    elif emotion == "sadness":

        tempo = 70
        notes = [60,63,67,70]

    elif emotion == "fear":

        tempo = 60
        notes = [40,41,45,46]

    elif emotion == "anger":

        tempo = 150
        notes = [50,55,57,62]

    else:

        tempo = 100
        notes = [60,64,67,72]

    midi.addTempo(track,time,tempo)

    for i in range(duration * 2):

        pitch = random.choice(notes)

        midi.addNote(track,0,pitch,time,1,100)

        time += 1

    with open("generated_music.mid","wb") as f:
        midi.writeFile(f)