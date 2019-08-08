import numpy as np
import cv2
import tkinter
from imutils.video import VideoStream
import uuid
import os
import yaml

# Set Variable only for Debugging Processes
DEBUG = True
# Define the side of the rectangle that represents the attention point. Side=2*R
R = 25
# Number of frames to save each time the program runs
NUM_OF_FRAMES = 100

# Create a unique user ID
UUID = uuid.uuid4().hex
print("The participant that is taking place has UUID:{}".format(UUID))
# Create the directories for the user
os.makedirs('dataset/' + UUID + '/positive')
os.makedirs('dataset/' + UUID + '/negative')

# Enable the camera
cap = VideoStream(src=0).start()
"""
Environment-agnostic way to get Screen Dimensions.
Tkinter is install with almost every python version.
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

data = dict(
    gender=gender,
    age=age,
    UUID=UUID,
    width=WIDTH,
    height=HEIGHT
)
with open('dataset/' + UUID + '/data.yml', 'w') as outfile:
    yaml.dump(data, outfile)

display_message = (
    "You are about to see {} consequtive screens. For each screen there are two options: If the screen \
contains a black dot look at the middle of it and press L(right hand). Else,look outside of the screen \
and press N.(left hand).\
\n\
\nWhen you are ready to start press Enter!").format(NUM_OF_FRAMES)
input(display_message)

# Initialize center to (0, 0). It will not affect the first frame though.
# It is used only to track the previous frame each time.
x, y = 0, 0
i = 0
while i < NUM_OF_FRAMES:
    not_looking = i%2

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
        bottom_left = ((int)(WIDTH/2) - 250, (int)(HEIGHT/2))
        cv2.putText(screen, "Look away from the screen and press N", bottom_left, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
    else:
        cv2.circle(screen, (x, y), R, (0, 255, 0), -1)

    # Proper way to display full screen
    cv2.namedWindow("Window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Window', screen)

    # Wait for answer key: L, N, Q or Z
    ans = cv2.waitKey(0)

    # Capture a frame immidiately after key hit
    frame = cap.read()

    if ans == ord('l'):
        i += 1
        cv2.imwrite(
            'dataset/' + UUID + '/positive/' + UUID + '_' + str(x) + '_' +
            str(y) + '.jpg', frame)
    elif ans == ord('n'):
        i += 1
        cv2.imwrite(
            'dataset/' + UUID + '/negative/' + UUID + '_' + str(x) + '_' +
            str(y) + '.jpg', frame)
    # Delete previous frame
    elif ans == ord('z'):
        prev_negative = 'dataset/' + UUID + '/negative/' + UUID + '_' + str(x_prev) + '_' + str(y_prev) + '.jpg'
        prev_positive = 'dataset/' + UUID + '/positive/' + UUID + '_' + str(x_prev) + '_' + str(y_prev) + '.jpg'

        if os.path.exists(prev_negative):
            os.remove(prev_negative)
        else:
            os.remove(prev_positive)
        i -= 1
    # Quit
    elif ans == 27:
        break
    else:
        print('You must press either l(looking) or n(not looking)')

# When everything is done, release the video capture
cap.stop()
cv2.destroyAllWindows()


"""
Feedback:
DONE -->1. Να γίνει diplay με text για να κοιτάξει αλλού.
DONE --> 2. Button για reset προηγούμενης τιμής.
3. Costa: Να ετοιμάσω pdf με οδηγίες. 
DONE --> 3. Costa: Consent. 
DONE --> 4. Αντί για rectangle να είναι κύκλος.
PLEASE EXPLAIN :) --> 5. Θέλουμε : Width/Height οθόνης, τι υπολογιστής είναι (screen dimensions)
PLEASE EXPLAIN :) --> 6. Structure fix 
7. Notebook αφού γραφτεί ο κώδικας.
8. Συλλογή από papers για citations και ενημέρωση.
"""

"""
Goals:
50 άτομα για αρχή,
100 για να είμαστε Happy.
"""