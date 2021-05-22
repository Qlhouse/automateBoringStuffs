# ffmpeg, static 是免编译版的
import re
import subprocess import check_call, PIPE, Popen

re_metadata = re.compile('Duration: (\d{2}):(\d{2}):(\d{2})\.\d+,.*\n.* (\d+(\.\d+)?) fps')

def get_metadata(filename):
    '''
    Get video metadata using ffmpeg
    '''
    p1 = 