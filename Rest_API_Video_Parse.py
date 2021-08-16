from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required = True)
video_put_args.add_argument("likes", type=str, help="Likes on the video is required", required = True)

#creating a dictionary of data to return
videos = {}

# abort if video does not exist
def stop_if_not_found(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

# this class is to deal with get , post etc
class Video(Resource):
    def get(self, video_id):
        stop_if_not_found(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    # def post(self):
    #     return {"data": "Posted"}


# register class as a resource, make it accesible through url
#<> user to write a string when passing a request - we are adding 'name ' to get method
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
