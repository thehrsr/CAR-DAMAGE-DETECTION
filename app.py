from flask import Flask, jsonify, request, render_template, send_file
import numpy as np
import skimage.io
import tensorflow as tf
import os
import io
import logging
import matplotlib.pyplot as plt
import cv2
import sys
import random
import math
import re
import time
import skimage
import glob

# Use Agg backend for Matplotlib
import matplotlib
matplotlib.use('Agg')

ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)

from mrcnn import model as modellib, visualize
from mrcnn.config import Config
from mrcnn.model import log
import custom

app = Flask(__name__)

# Root directory of the project
ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Path to trained weights file
MODEL_PATH = os.path.join(ROOT_DIR, "C:/Users/yy/Downloads/car3/mask_rcnn_damage_0007_19.h5")

# Define your custom configuration inline
class CustomConfig(custom.CustomConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 4  # Background + your custom class

config = CustomConfig()
config = custom.CustomConfig()


class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()

DEVICE = "/cpu:0"

def get_ax(rows=1, cols=1, size=16):
    """Return a Matplotlib Axes array to be used in
    all visualizations in the notebook. Provide a
    central point to control graph sizes.
    
    Adjust the size attribute to control how big to render images
    """
    _, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
    return ax

# Ensure default graph is used for prediction
global graph
graph = tf.compat.v1.get_default_graph()  # Updated to TensorFlow 2.x

# Create model object in inference mode.
with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on your custom dataset
model.load_weights(MODEL_PATH, by_name=True)

# Define your class names globally based on your dataset
class_names = ['BG', 'Scratch', 'Dent', 'Shatter', 'Dislocation']  # Adjust based on your dataset classes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'No file uploaded'})

    # Read the image
    image = skimage.io.imread(file)
    if image.ndim != 3:
        return jsonify({'error': 'Invalid image'})

    with graph.as_default():
        results = model.detect([image], verbose=1)
    
    # Extract the first result (assuming only one image)
    r = results[0]

    # Log the results using Mask R-CNN's log function
    log("rois", r['rois'])
    log("class_ids", r['class_ids'])
    log("scores", r['scores'])
    log("masks", r['masks'])

    # Create an image with the masks and bounding boxes
    fig, ax = plt.subplots(1, figsize=(12, 12))
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                                class_names, r['scores'], ax=ax)

    # Save the figure to a bytes object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png', bbox_inches='tight' )
    img_bytes.seek(0)
    plt.close(fig)

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
