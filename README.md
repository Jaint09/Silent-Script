# Silent-Script

Project Overview
This project is an AI-based application that converts hand gestures in sign language to text. The tool utilizes various Python machine learning libraries, including OpenCV for computer vision, MediaPipe for gesture detection, and TensorFlow for the machine learning model. The application processes live video input, detects hand gestures, and converts them into corresponding letters or words, allowing seamless communication with people using sign language.

Features
Real-time hand gesture recognition
Conversion of recognized gestures into text
Machine learning-based prediction model
Integration with OpenCV for image processing
Flask web application for a simple user interface
Requirements
To run this project, you will need Python 3.8+ and the following libraries installed. You can install the dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Python Libraries
The following Python libraries are used in this project:

absl-py==2.1.0
astunparse==1.6.3
attrs==24.2.0
blinker==1.8.2
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
click==8.1.7
cmake==3.30.4
colorama==0.4.6
contourpy==1.3.0
cvzone==1.6.1
cycler==0.12.1
dlib==19.24.1 (Pre-installed via wheel)
face-recognition==1.3.0
face_recognition_models==0.3.0
Flask==3.0.3
flatbuffers==24.3.25
fonttools==4.54.1
gast==0.6.0
google-pasta==0.2.0
greenlet==3.1.1
grpcio==1.66.2
h5py==3.12.1
idna==3.10
itsdangerous==2.2.0
jax==0.4.33
jaxlib==0.4.33
Jinja2==3.1.4
joblib==1.4.2
keras==3.5.0
kiwisolver==1.4.7
libclang==18.1.1
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==2.1.5
matplotlib==3.9.2
mdurl==0.1.2
mediapipe==0.10.14
ml-dtypes==0.4.1
namex==0.0.8
numpy==1.26.4
opencv-contrib-python==4.10.0.84
opencv-python==4.10.0.84
opt_einsum==3.4.0
optree==0.12.1
packaging==24.1
pillow==10.4.0
protobuf==4.25.5
pycparser==2.22
Pygments==2.18.0
pyparsing==3.1.4
python-dateutil==2.9.0.post0
requests==2.32.3
rich==13.9.1
scikit-learn==1.5.2
scipy==1.14.1
six==1.16.0
sounddevice==0.5.0
SQLAlchemy==2.0.35
tensorboard==2.17.1
tensorflow==2.17.0
tensorflow-intel==2.17.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.4.0
threadpoolctl==3.5.0
typing_extensions==4.12.2
urllib3==2.2.3
Werkzeug==3.0.4
wrapt==1.16.0
Installation
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/sign-language-to-text.git
cd sign-language-to-text
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Application:
To start the application:

bash
Copy code
python app.py
This will start a Flask server, which can be accessed through a web browser at http://127.0.0.1:5000.

Usage
Launch the application using the command above.
It will open a web page where you can start the camera.
Once the camera is active, the model will detect hand gestures in real time and convert them into corresponding text.
The predicted letters will be displayed on the screen as text.
Model Training
To train the machine learning model for recognizing hand gestures:

Prepare the dataset: You can collect images of different hand gestures and label them accordingly.
Train the model: Use the provided train.py script to train your model. Ensure that TensorFlow and Keras are installed correctly.
bash
Copy code
python train.py
Future Enhancements
Adding support for converting gestures into full sentences rather than just individual letters.
Improving accuracy with more comprehensive datasets.
Integrating the application with speech synthesis for text-to-speech conversion.
Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

License
This project is licensed under the MIT License.
