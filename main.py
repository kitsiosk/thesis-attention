import numpy as np
import cv2
import pyscreenshot as ImageGrab
from imutils.video import VideoStream
import uuid

# Create a unique user ID
UUID = uuid.uuid4().hex

# Enable the camera
cap = VideoStream(src=0).start()

# Take a screenshot to calculate screen dimensions. It is saved in Pillow format
screenshot = ImageGrab.grab()
# Convert it to opencv format
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# Save the screen height and width
HEIGHT = screenshot.shape[0] 
WIDTH = screenshot.shape[1]
# Define the side of the rectangle that represents the attention point. Side=2*R
R = 10
# Number of frames to save each time the program runs
NUM_OF_FRAMES = 3

# Personal data colelction and validation
print('Hello, we would like to collect data about your gender and age.')
while True:
    gender = input('Press \'f\' for female and \'m\' for male ')
    if gender == 'm' or gender == 'f':
        break
while True:
    age = input('Please input your age in years')
    if age.isdigit():
        break

 
print('You will see 3 consequtive white screens with a black point somewhere. We need you to press either the upkey or the downkey at each screen depending on wether you are looking at the black point directly(then press the upkey at that very moment) or looking at any other point of the screen (then press the downkey at that very moment).')
input('When you are ready, press enter to start!')

i=0
while i < NUM_OF_FRAMES:
    # Initialize a white screen
    screen = np.ones((HEIGHT, WIDTH))

    # Choose a random point on the screen
    x = np.random.randint(R, WIDTH-R)
    y = np.random.randint(R+100, HEIGHT-R-100)

    # Color black the rectangle of side 2R and center the point (x, y)
    screen[y-R:y+R, x-R:x+R] = 0

    cv2.imshow('screen', screen)
    ans = cv2.waitKey(0)

    frame = cap.read()

    # 82 is the integer value for 'up' key
    # 84 is the integer value for 'down' key
    if ans == 82:
        i+=1
        cv2.imwrite('dataset/positives/' + UUID + '_' + str(x) + '_' + str(y) + '.jpg', frame)
    elif ans == 84:
        i+=1
        cv2.imwrite('dataset/negatives/' + UUID + '_' + str(x) + '_' + str(y) + '.jpg', frame)
    else:
        print('You must press either upkey or downkey')

# When everything is done, release the video capture
cap.stop()
cv2.destroyAllWindows()