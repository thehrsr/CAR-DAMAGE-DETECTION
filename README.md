# Mask R-CNN Car Damage Prediction

This project is a web-based application that utilizes a pre-trained Mask R-CNN model to predict and classify different types of car damage from images. The model is trained to detect and label scratches, dents, shatters, and dislocations on car bodies.

## Features

- Upload an image of a car and detect damage.
- Classify the type of damage (scratch, dent, shatter, dislocation).
- Visualize the damage with bounding boxes and masks.

  ## Demo

![Screenshot 2024-08-31 052704](https://github.com/user-attachments/assets/75de5ffe-6080-456f-8d94-5a154ac5778b)


![Screenshot 2024-08-31 053152](https://github.com/user-attachments/assets/def8a406-e83f-4e7a-90a7-439758c71ec5)


![Screenshot 2024-07-10 102943](https://github.com/user-attachments/assets/dcc20a46-38d1-4ca4-9f5d-68c5f5ffd64b)


![Screenshot 2024-06-21 161627](https://github.com/user-attachments/assets/65728994-78c9-4664-9895-9c0c44261beb)


![Screenshot 2024-07-19 180607](https://github.com/user-attachments/assets/794e4591-80b9-485b-ba32-da49fc53cae0)


![Screenshot 2024-08-31 053946](https://github.com/user-attachments/assets/3dbb6439-f606-4ebb-8381-73f36d6418ba)


![Screenshot 2024-08-31 054007](https://github.com/user-attachments/assets/06b4560b-06cd-4910-b941-c723b82146d3)


![Screenshot 2024-08-31 054024](https://github.com/user-attachments/assets/beb93cce-7b19-4c14-a2cd-541383dad4a8)



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
![Screenshot 2024-08-31 052354](https://github.com/user-attachments/assets/3044a684-6d04-4af1-a947-44d53547c4c7)

Click the "Choose Image" button to upload an image of a car.
![Screenshot 2024-08-31 052450](https://github.com/user-attachments/assets/91a737b2-4e44-49e7-a8e3-c18bd932c1c8)
![Screenshot 2024-08-31 052518](https://github.com/user-attachments/assets/c0c7b16c-50ff-47c0-a4a4-c8f716cc8721)
![Screenshot 2024-08-31 052543](https://github.com/user-attachments/assets/e5947548-0b43-4afd-bff7-da2a6e8c9a91)



Click "Upload" to submit the image.
The application will display the detected damages with bounding boxes and masks.
![Screenshot 2024-08-31 052611](https://github.com/user-attachments/assets/aa47ed11-2dcf-4798-bf77-1a6349131e9e)





### Workflow
Bounding Boxes

![Screenshot 2024-08-31 054126](https://github.com/user-attachments/assets/6785cc21-4cbe-41f3-a674-bf17b0d10f5d)

ROIs

![Screenshot 2024-08-31 054150](https://github.com/user-attachments/assets/29636c34-8a17-439f-9df9-45134bd4c4fd)

Anchors

![Screenshot 2024-08-31 054207](https://github.com/user-attachments/assets/7d8264ad-2149-48ad-aa22-c2aa33cdc69a)

![Screenshot 2024-08-31 054225](https://github.com/user-attachments/assets/c1d73d99-94ac-4c4b-a822-c9843076a0a7)


### Troubleshooting
If you encounter issues with the Flask server, ensure that all dependencies are installed correctly.
If you receive a KeyError: 'file' error, check the form submission in the frontend and ensure the file input is correctly named.

