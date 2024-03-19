import os

os.system("pip install sox")

import sox

import subprocess

# Get all audio files in the current directory
audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]

# Loop through the audio files and apply voice restoration
for audio_file in audio_files:
    # Create a new file name for the restored audio
    restored_file = audio_file.replace('.wav', '_restored.wav')

    # Apply voice restoration using Sox
    subprocess.call(['sox', audio_file, restored_file, 'vad'])

# softy_plug