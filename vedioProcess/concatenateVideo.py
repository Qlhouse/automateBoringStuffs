from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
import os

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
source_path2 = os.path.join(SAMPLE_INPUTS, 'joke.webm')

output_path = os.path.join(SAMPLE_OUTPUTS, 'output.mp4')

# Resize clip
clip = VideoFileClip(source_path).subclip(t_start=(0, 1, 10), t_end=(0, 1, 30))
clip_resized = clip.fx(vfx.resize, 0.5)
# clip_resized.write_videofile(output_path)


# Set audio from another vedio
clip2 = VideoFileClip(source_path2).subclip(t_start=(0, 0, 20), t_end=(0, 0, 40))
clip3 = clip2.set_audio(clip.audio).resize(width=800)
# clip3.write_videofile(output_path)


# Combine video
# List of videos should has the same size
clip4 = concatenate_videoclips([clip, clip2])
# clip4.write_videofile(output_path)


# Concatenate array video
clip5 = clip2.fx(vfx.mirror_y)
outputClip = clips_array([[clip, clip2],
                         [clip3, clip5]])
# outputClip.write_videofile(output_path)


# Conposite videos
composite_clip = CompositeVideoClip([clip, 
                                     clip3.set_position(lambda t: (5*t, 5*t)).set_start(5).crossfadein(3)])

composite_clip.write_videofile(output_path)                                    