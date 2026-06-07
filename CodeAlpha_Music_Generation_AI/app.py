import streamlit as st
from music21 import stream, note
import random

st.set_page_config(page_title="AI Music Generator", page_icon="🎵")

st.title("🎵 AI Music Generation System")
st.write("Generate simple AI-created music and save it as a MIDI file.")

if st.button("Generate Music"):

    notes = [
        'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
        'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5'
    ]

    melody = stream.Stream()

    for _ in range(60):
        new_note = note.Note(random.choice(notes))
        new_note.quarterLength = random.choice(
            [0.25, 0.5, 1, 1.5]
        )
        melody.append(new_note)

    filename = "generated_music.mid"

    melody.write('midi', fp=filename)

    st.success("Music generated successfully!")

    with open(filename, "rb") as file:
        st.download_button(
            label="⬇️ Download MIDI File",
            data=file,
            file_name="generated_music.mid",
            mime="audio/midi"
        )

st.info("Click the button to generate a new music sequence.")