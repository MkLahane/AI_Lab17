from flask import Flask, render_template, url_for, send_from_directory, request
from io import BytesIO
import numpy as np
import base64
from PIL import Image, ImageOps
import tensorflow as tf

app = Flask(__name__)
json_file = open('./model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = tf.keras.models.model_from_json(loaded_model_json)
model.load_weights("./model/model.h5")

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit_image():
    data = request.get_json()
    image_b64 = data['base64'].split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_b64)))
    IMG_SHAPE = (28, 28)
    image = ImageOps.grayscale(image)
    image = image.resize(IMG_SHAPE)
    np_arr = np.array(image)
    np_arr = np.expand_dims(np_arr, -1)
    np_arr = np_arr.astype("float32") / 255
    label = np.argmax(model.predict(np.array([np_arr])))
    return {"label": str(label)}

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run()