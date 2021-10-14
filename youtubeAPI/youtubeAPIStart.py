from googleapiclient.discovery import build

api_key ='AIzaSyD3YCpuiDzQLcHruTiSovuUi-0s-bFJeck'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part = 'statistics',
    forUsername = 'scahfer5'
)

response = request.execute()

print(response)