import os
from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
import werkzeug
from werkzeug.utils import secure_filename
from utils.makeImage import makeDotImg
import cv2
import io

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER = './uploads'
OUTPUT_DIR = 'outputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class ImageAPI(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
    parser.add_argument('colors', type=int)
    parser.add_argument('ratio', type=float)
    query_data = parser.parse_args()
    ratio = query_data['ratio']
    colors = query_data['colors']
    file = query_data['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    output = makeDotImg(filepath, r = ratio, c = colors)
    is_success, buffer = cv2.imencode(".jpg", output)
    io_buf = io.BytesIO(buffer)
    io_buf.seek(0)
    return send_file(io_buf, as_attachment=True, download_name=filename, mimetype='image/jpeg')
api.add_resource(ImageAPI, '/img', endpoint='img')

if __name__ == '__main__':
  app.run(debug=True)