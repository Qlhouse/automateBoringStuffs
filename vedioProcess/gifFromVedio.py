from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os
# from moviepy.video.fx.all import resize

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)

output_path = os.path.join(GIF_DIR, 'sample.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10, 30).resize(width=500)

subclip.write_gif(output_path, fps=20, program='ffmpeg')