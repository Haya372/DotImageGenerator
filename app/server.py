from typing import BinaryIO
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from utils.makeImage import makeDotImg

app = Flask(__name__)
api = Api(app)

class ImageAPI(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
    query_data = parser.parse_args()
    print(query_data)
    return "ok"
api.add_resource(ImageAPI, '/img', endpoint='img')

if __name__ == '__main__':
    app.run(debug=True)