from youtube_statistics import  YTstats

API_KEY ='AIzaSyD3YCpuiDzQLcHruTiSovuUi-0s-bFJeck'
channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'

yt = YTstats(API_KEY, channel_id)
# yt.get_channel_statistics()
# yt.dump()
yt.get_channel_video_data()