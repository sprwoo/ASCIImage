# Imports
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Flask upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        img = Image.open(file.stream)
        extracted_text = get_ascii_text(img)
        return jsonify({"ascii_text": extracted_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Constants
DENSITIES = "  .'`^\",:;Il!i~+_-?][}{1)(|\\/#MW&8%B@$"
RESIZE = (50, 50)
NTSC_CONST = np.array([0.2989, 0.587, 0.114])

def NTSC_formula(rgb):
    return np.dot(rgb, NTSC_CONST.T)

def density_character(val):
    tmp = math.floor(val / (255 / len(DENSITIES)))
    return DENSITIES[tmp]

def convert_to_ascii(image_array, height, width, channels):
    row = ""
    for i in range(height):
        for j in range(width):
            pixel = NTSC_formula(image_array[i][j][:3])
            asciichar = density_character(pixel)
            if (asciichar == " "):
                asciichar = "&nbsp;"
            row += asciichar
        row += "<br>"
    return row

def get_ascii_text(image):
    if image is None:
        raise ValueError("No image provided")

    image = image.resize(RESIZE)
    image_array = np.array(image)
    height, width, channels = image_array.shape
    ascii_image = convert_to_ascii(image_array, height, width, channels)
    return ascii_image
