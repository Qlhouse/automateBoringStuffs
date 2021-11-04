from moviepy.editor import *

BASE_DIR = "/home/admin/"
audioFile = "Demystifying[01].webm"
videoFile = "Demystifying Python_s Async and Await Keywords[00].webm"
outputFile = BASE_DIR + "Demystifying Python_s Async and Await Keywords.webm"

# Extract audio from file
# print(BASE_DIR + audioFile)
audioClip = AudioFileClip(BASE_DIR + audioFile)
# clip.audio.write_audiofile('classicYueYuSongs.wav', codec='pcm_s16le')

videoClip = VideoFileClip(BASE_DIR + videoFile)

videoClip.set_audio(audioClip)

videoClip.write_videofile(outputFile)