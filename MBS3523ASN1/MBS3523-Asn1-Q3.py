import cv2
import time
import numpy as np
import random

# capture frames from a video
cap = cv2.VideoCapture('resources/002.mp4')
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('resources/cars.xml')
face = cv2.CascadeClassifier('resources/fullbody.xml')
# loop runs if capturing has been initialized.
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    color= random.randint(0,256)
    color2 = random.randint(0, 256)
    color3= random.randint(0, 256)
    cars = car_cascade.detectMultiScale(gray, 1.4, 2)
    hum = face.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in hum:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (color,color2,color3), 2)
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h),(color3,color2,color) , 2)
        cv2.imshow('Detection', frames)
    if cv2.waitKey(100) == 27:
        break
cap.release()
cv2.destroyAllWindows()