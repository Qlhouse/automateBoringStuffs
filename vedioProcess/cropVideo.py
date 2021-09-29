from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

output_path = os.path.join(SAMPLE_OUTPUTS, 'output.mp4')

# Set audio from another vedio
clip = VideoFileClip(source_path).subclip(t_start=(0, 4, 35), t_end=(0, 6, 43))
clip3 = clip.resize(width=800)
clip3.write_videofile(output_path)