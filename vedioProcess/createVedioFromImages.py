from ntpath import join
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

output_vedio = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')

os.makedirs(thumbnail_dir, exist_ok=True)

this_dir = os.listdir(thumbnail_dir)

filepaths = [os.path.join(thumbnail_dir, fname) for 
    fname in this_dir if fname.endswith(".jpg")]

clip = ImageSequenceClip(filepaths, fps=4)
clip.write_videofile(output_vedio)
