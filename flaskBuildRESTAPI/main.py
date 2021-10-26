from flask import  Flask
from flask_restful import  Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video is required", required=True)

videos = {}

def abort_if_videoID_doesnot_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Could not find video ...")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message='Video already exists with that ID ...')

class Video(Resource):
    def get(self, video_id):
        abort_if_videoID_doesnot_exist(video_id)
        return videos[video_id]
    ''' Test case
    import  requests

    BASE = 'http://127.0.0.1:5000/'
    
    response = requests.get(BASE + 'video/6')
    print(response.json())
    '''

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        print(videos[video_id])
        return videos[video_id], 201
    ''' Test case
    import  requests

    BASE = 'http://127.0.0.1:5000/'

    response = requests.put(BASE + 'video/1', {"likes": 10, 'name': 'John', 'views': 100})
    print(response.json())
    input()
    response = requests.get(BASE + 'video/6')
    print(response.json())
    '''

    def delete(self, video_id):
        abort_if_videoID_doesnot_exist(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)