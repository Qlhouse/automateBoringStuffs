import speech_recognition as sr

recognizer = sr.Recognizer()

# Energy threshold: You can think of the energy threshold as the loudness 
# of the audio files. The values below the threshold are considered silent, 
# and the values above the threshold are considered speech.
recognizer.energy_threshold = 300

# Speech Recognition has a built-in function to make it work with many of the
# APIs out there.

# file = 
audio_file = sr.AudioFile(f"C:\Users\john\Documents\automateBoringStuffs\speechRecognition\my_audio.wav")

# Speech Recognition's built-in function recognize_google() is free and 
# doesn't require an API key to use.
with audio_file as source:
    audio = recognizer.record(source)
    recognizer.recognize_google(audio_data=audio, language="en-US")

