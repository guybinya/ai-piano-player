import tkinter as tk

from piano.notes import notes, available_chords
from piano.player import Synth


def create_piano_note_buttons(root, synth: Synth):
    # Create buttons for each piano note
    for note_name, midi_note in notes.items():
        button = tk.Button(root, text=note_name, command=lambda n=midi_note: synth.play_note(n))
        button.pack(side=tk.LEFT, padx=10, pady=10)
    return root


# Function to add buttons for chords to the Tkinter window
def add_chord_buttons(root, chords, synth: Synth):
    for chord_name, notes in chords.items():
        # Command to play chord when button is pressed
        button_command = lambda n=notes: synth.play_chord(n, 80, 1000)
        # Create the button and pack it into the GUI
        button = tk.Button(root, text=chord_name, command=button_command)
        button.pack()
    return root


def setup_ui():
    # Set up the tkinter GUI window
    root = tk.Tk()
    # Initialize FluidSynth with a SoundFont
    synth = Synth(root)
    root.title("Piano Simulator")
    # Add note buttons to the GUI
    root = create_piano_note_buttons(root, synth=synth)
    # Add chord buttons to the GUI
    root = add_chord_buttons(root, available_chords, synth=synth)
    # Add GPT button to the GUI
    button = tk.Button(root, text="GPT", command=synth.play_openai_chords)
    button.pack()
    return root

