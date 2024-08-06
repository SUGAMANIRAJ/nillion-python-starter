import cv2
import numpy as np
import os
from nada_dsl import *
import nada_numpy as na

from tensorflow.keras.models import load_model

# Load the VGG19 model
vgg_model = load_model("/content/drive/MyDrive/Deepfakedetectiondataset/vgg_model.h5")
vgg_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load the ResNet50 model
resnet_model = load_model("/content/drive/MyDrive/Deepfakedetectiondataset/resnet_model.h5")
resnet_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



def extract_frames(video_path, num_frames=10):
    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % (cap.get(cv2.CAP_PROP_FRAME_COUNT) // num_frames) == 0:
            frame = cv2.resize(frame, (224, 224))
            frame = frame / 255.0
            frame = np.expand_dims(frame, axis=0)
            frames.append(frame)
        frame_count += 1
    cap.release()
    frames = np.concatenate(frames, axis=0)
    return frames

input_video_path = os.sys.argv[1]

# Preprocess the input video frames
input_frames = extract_frames("/content/drive/MyDrive/Deepfakedetectiondataset/arjdbfrxvufk.mp4",num_frames=10)
input_frames = np.array(input_frames)
input_frames = input_frames / 255.0

vgg_predictions = na.array(vgg_model.predict(input_frames, verbose=0))
resnet_predictions = na.array(resnet_model.predict(input_frames, verbose=0))

# Count the number of predictions for each class (0: real, 1: fake)
class_counts = np.bincount([np.argmax(vgg_predictions), np.argmax(resnet_predictions)])

# Get the index of the class with the highest count
final_prediction = np.argmax(class_counts)

# Print the final prediction
if final_prediction == 0:
    print("REAL")
else:
    print("FAKE")