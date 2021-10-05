import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from werkzeug.utils import secure_filename
from utils.makeImage import makeDotImg

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class ImageAPI(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
    query_data = parser.parse_args()
    file = query_data['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "ok"
api.add_resource(ImageAPI, '/img', endpoint='img')

if __name__ == '__main__':
    app.run(debug=True)