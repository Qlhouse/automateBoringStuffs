from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')

os.makedirs(thumbnail_dir, exist_ok=True)

clip = VideoFileClip(source_path)

duration = clip.duration

def getPerSecondFrameImage():
    max_duration = int(duration) + 1
    for i in range(0, max_duration):
        # print(f"frame at {i} seconds")
        frame = clip.get_frame(i)
        new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
        newImg = Image.fromarray(frame)
        newImg.save(new_img_filepath)

def getInterFrameImage():
    for i, frame in enumerate(clip.iter_frames()):
        # print(f"frame at {i} seconds")
        interFrame_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
        newImg = Image.fromarray(frame)
        newImg.save(interFrame_img_filepath)

getInterFrameImage()
