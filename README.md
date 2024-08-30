# Mask R-CNN Car Damage Prediction

This project is a web-based application that utilizes a pre-trained Mask R-CNN model to predict and classify different types of car damage from images. The model is trained to detect and label scratches, dents, shatters, and dislocations on car bodies.

## Features

- Upload an image of a car and detect damage.
- Classify the type of damage (scratch, dent, shatter, dislocation).
- Visualize the damage with bounding boxes and masks.

  ## Demo

![Demo Image](Screenshot 2024-![Screenshot 2024-06-21 161627](https://github.com/user-attachments/assets/3f36a6ef-b49c-4988-b15f-16d1169ddbc7)


## Project Structure

- `app.py`: The main Flask application that serves the web interface and handles image processing requests.
- `custom.py`: Contains the custom configuration for the Mask R-CNN model.
- `templates/index.html`: The HTML template for the web interface.
- `static/`: Contains static files like CSS and images.
- `logs/`: Directory for storing logs and trained model files.

## Installation

### 1. Clone the Repository


git clone https://github.com/the_hrsr/mask_rcnn_car_damage_prediction.git
cd mask_rcnn_car_damage_prediction

###  2. Create and Activate a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Train the model
Train the model using jupyter notebook and replace the h5 file.

### 5. Run the Application
 Run the Application


The application will start and run on http://127.0.0.1:5000/.

### Usage
Open your browser and navigate to http://127.0.0.1:5000/.
Click the "Choose Image" button to upload an image of a car.
Click "Upload" to submit the image.
The application will display the detected damages with bounding boxes and masks.


### Troubleshooting
If you encounter issues with the Flask server, ensure that all dependencies are installed correctly.
If you receive a KeyError: 'file' error, check the form submission in the frontend and ensure the file input is correctly named.

