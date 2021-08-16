from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

#creating a dictionary of data to return
names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"},
         "graza": {"age": 25, "gender": "female"}}

# this class is to deal with get , post etc
class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    # def post(self):
    #     return {"data": "Posted"}


# register class as a resource, make it accesible through url
#<> user to write a string when passing a request - we are adding 'name ' to get method
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)


