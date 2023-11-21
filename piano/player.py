# MIDI note numbers for a one-octave C major scale
import os
import time

import fluidsynth

import ai_agent
from chord_types import Chord
from piano.notes import available_chords, chord_names


class Synth:
    fs = None
    root = None

    def __init__(self, root):
        self.fs = init_fluidsynth()
        self.root = root

    def stop(self):
        # Stop the FluidSynth synthesizer when done
        self.fs.delete()

    def play_note(self, note: int, ms=1000):
        self.fs.noteon(0, note, 127)  # channel 0, velocity 127
        self.root.after(ms, lambda: self.fs.noteoff(0, note))  # Note off after 1 sec

    def play_chord(self, notes_to_play: list[int], velocity: int, ms: int):
        # Play each note in the chord
        for note in notes_to_play:
            self.fs.noteon(0, note, velocity)  # channel 0, velocity 80
        time.sleep(1)  # hold chord for 1 second
        # Turn off each note in the chord
        for note in notes_to_play:
            self.fs.noteoff(0, note)

    def play_progression(self, chords_array: list[Chord]):
        print("Chord progression is playing: ", str(chords_array))
        for chord_obj in chords_array:
            if chord_obj['chord_name'] in available_chords:
                print('Playing: ', chord_obj)
                self.play_chord(notes_to_play=available_chords[chord_obj['chord_name']], velocity=chord_obj['velocity'],
                                ms=chord_obj['time'])
            else:
                print(f"Received an unrecognized chord: {chord_obj}")

    def play_openai_chords(self):
        chords_array = ai_agent.get_chords_from_openai(chord_names)
        self.play_progression(chords_array)


def init_fluidsynth():
    fs = fluidsynth.Synth()
    fs.start(driver="coreaudio")
    sfid = fs.sfload(get_sf_path())
    fs.program_select(0, sfid, 0, 0)
    return fs


def get_sf_path():
    variable_name = "PATH_TO_SF"
    variable_value = os.environ.get(variable_name)
    return variable_value
