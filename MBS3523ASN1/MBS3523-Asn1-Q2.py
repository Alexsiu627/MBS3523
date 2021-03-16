import cv2
#import numpy as np
import random
print(cv2.__version__)

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(1)
# Below 2 lines are used to set the webcam window size
capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame
x = 0
y = 0
dx = 1
dy = 1
color = random.randint(0, 256)
color2 = random.randint(0, 256)
color3 = random.randint(0, 256)

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.rectangle(img,(x,y),(x+50,y+50),(color,color2,color3),3)
    x = x + dx
    y = y + dy
    if x >= 590 or x <= 0:
        dx = dx * (-1)
    if y >= 430 or y <= 0:
        dy = dy * (-1)
    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == 27:
        break

capture.release()
cv2.destroyAllWindows()