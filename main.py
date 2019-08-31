import numpy as np
import cv2
import tkinter
from imutils.video import VideoStream, WebcamVideoStream
import uuid
import os
from sys import platform
import yaml
import time

# Set Variable only for Debugging Processes
DEBUG = False
# Define the radius of the circle that represents the attention point
R = 25
# Number of frames to save each time the program runs
NUM_OF_FRAMES = 52

# Create a unique user ID
UUID = uuid.uuid4().hex
print("The participant that is taking place has UUID:{}".format(UUID))
# Create the directories for the user
os.makedirs('dataset/' + UUID + '/positive')
os.makedirs('dataset/' + UUID + '/negative')

# Enable the camera
cap = cv2.VideoCapture(0)
"""
Environment-agnostic way to get Screen Dimensions.
Tkinter is installed with almost every python version.
Plus there is no need for external Library and I/O.
"""
root = tkinter.Tk()
root.withdraw()
WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()
if DEBUG: print("Width is {} and Height is {}".format(WIDTH, HEIGHT))

# Personal data colelction and validation
print('Hello, we would like to collect data about your gender and age.')
while True:
    gender = input('Press \'f\' for female OR \'m\' for male ')
    if gender == 'm' or gender == 'f':
        break
while True:
    age = input('Please input your age in years:')
    if age.isdigit():
        age = int(age)
        break
while True:
    laptop_message = "Which laptop are you using? Press\
 C for Costas K for Kitsios U for Unknown"

    laptop = input(laptop_message)
    if laptop == "k" or laptop == "c" or laptop == "u" or \
        laptop == "K" or laptop == "C" or laptop == "U":
        break

data = dict(gender=gender,
            age=age,
            UUID=UUID,
            width=WIDTH,
            height=HEIGHT,
            laptop=laptop)

with open('dataset/' + UUID + '/data.yml', 'w') as outfile:
    yaml.dump(data, outfile)

print("Testing camera stream. Press \'q\' when camera is set")
# Test camera stream
while (True):
    # Capture frame-by-frame
    _, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# Clear the terminal before showing instructions message
# print("\033c", end="")
display_message = (
    "You are about to see {} consequtive screens. For each screen there are two options: If the screen \
contains a black dot look at the middle of it and press space. Otherwise, look outside of the screen \
and press space. Each time space is hit the screen changes\
\n\
\nWhen you are ready to start press Enter!").format(NUM_OF_FRAMES)
input(display_message)

# Initialize center to (0, 0). It will not affect the first frame though.
# It is used only to track the previous frame each time.
x, y = 0, 0
i = 0

while i < NUM_OF_FRAMES:
    # Variable determining wether we should show a "looking" screen
    # or a "not looking" screen. Set to i%2 so the screens show in turn
    not_looking = (i >= NUM_OF_FRAMES / 2 + 1) or (i == 1)

    # Initialize a white screen
    screen = np.ones((HEIGHT, WIDTH))
    # Save the previous center before generating a new one
    # in order to be able to delete it.
    x_prev, y_prev = x, y

    # Choose a random point on the screen
    x = np.random.randint(R, WIDTH - R)
    y = np.random.randint(R + 100, HEIGHT - R - 100)

    # If the user is supposed to not look, show a relevant text on screen
    # Else show the point of attention
    if not_looking:
        bottom_left = ((int)(WIDTH / 2) - 250, (int)(HEIGHT / 2))
        cv2.putText(screen,
                    "Look away from the screen and press space",
                    bottom_left,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 0, 0),
                    lineType=cv2.LINE_AA)
    else:
        cv2.circle(screen, (x, y), R, (0, 255, 0), -1)

    if platform == "linux" or platform == "linux2":
        # Proper way to display full screen in Linux
        cv2.namedWindow("Window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Window', screen)
    else:
        # Proper way to display full screen on Macos
        cv2.imshow('Window', screen)
        cv2.namedWindow("Window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)

    # Wait for answer key: Space, Esc or Z
    ans = cv2.waitKey(0)

    # Capture a frame immidiately after key hit
    _, frame = cap.read()
    time.sleep(0.2)

    if ans == ord(' '):
        if not DEBUG:
            if (not not_looking):
                cv2.imwrite(
                    'dataset/' + UUID + '/positive/' + UUID + '_' + str(x) +
                    '_' + str(y) + '.jpg', frame)
            else:
                cv2.imwrite(
                    'dataset/' + UUID + '/negative/' + UUID + '_' + str(x) +
                    '_' + str(y) + '.jpg', frame)
        i += 1
    # Delete previous frame
    elif ans == ord('z'):
        prev_negative = 'dataset/' + UUID + '/negative/' + UUID + '_' + str(
            x_prev) + '_' + str(y_prev) + '.jpg'
        prev_positive = 'dataset/' + UUID + '/positive/' + UUID + '_' + str(
            x_prev) + '_' + str(y_prev) + '.jpg'

        if os.path.exists(prev_negative):
            os.remove(prev_negative)
        else:
            os.remove(prev_positive)
        i -= 1
    # Quit
    elif ans == ord('q'):
        break
    else:
        print('You must press either Space, Esc or Z')

# When everything is done, release the video capture
cap.release()
cv2.destroyAllWindows()
"""
Feedback:
DONE -->1. Να γίνει diplay με text για να κοιτάξει αλλού.
DONE --> 2. Button για reset προηγούμενης τιμής.
3. Costa: Να ετοιμάσω pdf με οδηγίες. 
DONE --> 3. Costa: Consent. 
DONE --> 4. Αντί για rectangle να είναι κύκλος.
DONE --> 5. Θέλουμε : Width/Height οθόνης, τι υπολογιστής είναι (screen dimensions)
DONE --> 6. Structure fix 
7. Notebook αφού γραφτεί ο κώδικας.
8. Συλλογή από papers για citations και ενημέρωση.
"""
"""
Goals:
50 άτομα για αρχή,
100 για να είμαστε Happy.
"""