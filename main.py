import numpy as np
import cv2
import time
import pyscreenshot as ImageGrab
from imutils import face_utils
from imutils.video import VideoStream
import dlib

cap = VideoStream(src=0).start()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlib/shape_predictor_68_face_landmarks.dat')

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# Take a screenshot to calculate screen res. It is saved in Pillow format
screenshot = ImageGrab.grab()
# Convert it to opencv format
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# Save the screen height and width
HEIGHT = screenshot.shape[0] 
WIDTH = screenshot.shape[1]
R = 10

# Initialize a white screen
screen = np.ones((HEIGHT, WIDTH))

# Choose a random point on the screen
x = np.random.randint(R, WIDTH-R)
y = np.random.randint(R, HEIGHT-R)

# Color black the rectangle of side 2R and center the point (x, y)
screen[y-R:y+R, x-R:x+R] = 0

print('Are you looking to the black point?')
cv2.imshow('screen', screen)
ans = cv2.waitKey(0)

frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# detect the face in the grayscale frame
rect = detector(gray, 0)[0]

# determine the facial landmarks for the face region, then
# convert the facial landmark (x, y)-coordinates to a NumPy
# array
shape = predictor(gray, rect)
shape = face_utils.shape_to_np(shape)

# extract the left and right eye coordinates
leftEye = shape[lStart:lEnd]
rightEye = shape[rStart:rEnd]

# concatenate the coordinates of the two eyes in a single
# landmarks array
landmarks = np.concatenate((leftEye, rightEye), axis=0)

# loop over the (x, y)-coordinates of the eyes
# and draw them on the image
for (x, y) in landmarks:
    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

# Display the resulting frame
cv2.imshow('frame', frame)
cv2.waitKey(0)

print(ans)
print(x)
print(y)

# When everything done, release the capture
cap.stop()
cv2.destroyAllWindows()