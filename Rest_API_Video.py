from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

#creating a dictionary of data to return
Videos = {}

# this class is to deal with get , post etc
class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form['likes'])
        return {}

    # def post(self):
    #     return {"data": "Posted"}


# register class as a resource, make it accesible through url
#<> user to write a string when passing a request - we are adding 'name ' to get method
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)


