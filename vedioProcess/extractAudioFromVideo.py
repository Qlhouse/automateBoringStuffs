from moviepy.editor import *

clip = VideoFileClip(r'D:\machineLearning\classicYueYuSongs.mp4')

# Write out audio file
clip.audio.write_audiofile('classicYueYuSongs.wav', codec='pcm_s16le')