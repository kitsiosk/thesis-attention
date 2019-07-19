import numpy as np
import cv2
import tkinter
from imutils.video import VideoStream
import uuid

# Set Variable only for Debugging Processes
DEBUG = True
# Define the side of the rectangle that represents the attention point. Side=2*R
R = 25
# Number of frames to save each time the program runs
NUM_OF_FRAMES = 3

# Create a unique user ID
UUID = uuid.uuid4().hex
print("The participant that is taking place has UUID:{}".format(UUID))

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
        break
"""
Feedback:
I suggest rather than saying press Down or Up key to make it even more self-explanatory.
Press L when Looking. 
Press N when No Looking.
"""
display_message = (
    "When you see a dot at the screen, look at the middle of it and press L(right hand). Else look outside the screen and press N.(left hand).\
\n\
\nWhen you are ready to start press Enter!").format(NUM_OF_FRAMES)

input(display_message)

i = 0
while i < NUM_OF_FRAMES:
    # Initialize a white screen
    screen = np.ones((HEIGHT, WIDTH))

    # Choose a random point on the screen
    x = np.random.randint(R, WIDTH - R)
    y = np.random.randint(R + 100, HEIGHT - R - 100)

    # Color black the rectangle of side 2R and center the point (x, y)
    screen[y - R:y + R, x - R:x + R] = 0

    # Proper way to display full screen
    cv2.namedWindow("Window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Window', screen)
    ans = cv2.waitKey(0)

    frame = cap.read()
    """
    Feedback:
    Οι φάκελοι καλό θα ήταν σε πρώτο βάθος να χωρίζονται με βάση το UUID.
    Αυτό γιατί αν γίνει fail από κάποιο άτομο και μας το πει εκείνη την στιγμή να είμαστε σε
    θέση να διαγράψουμε απευθείας τα δεδομένα του από τον φάκελο και να κάνουμε καινούρια έρευνα.
    """
    """
    Feedback:
    Δεν υπήρχε κάποιο key για να σταματάει η έρευνα. Ειδικά σε debug mode είναι αναγκαίο.
    Έβαλα το ESC σε αυτήν την περίπτωση.
    """

    # 82 is the integer value for 'up' key
    # 84 is the integer value for 'down' key
    if ans == ord('l'):
        i += 1
        cv2.imwrite(
            'dataset/positives/' + UUID + '_' + str(x) + '_' + str(y) + '.jpg',
            frame)
    elif ans == ord('n'):
        i += 1
        cv2.imwrite(
            'dataset/negatives/' + UUID + '_' + str(x) + '_' + str(y) + '.jpg',
            frame)
    elif ans == 27:
        break
    else:
        print('You must press either upkey or downkey')

# When everything is done, release the video capture
cap.stop()
cv2.destroyAllWindows()
"""
Feedback:
Now regarding the data structure my advice would be to modify the way you save the participants.
The optimal suggested structure I can think of is the following:
Dataset
└── UUID_of_Participant
    ├── data.yml
    ├── negative
    │   └── UUID_newUUIDfortheImage.jpg
    └── positive
        └── UUID_posX_posY.jpg
    .
    .
    .
    UUID_of_other_Participant

I have left you with an example of only a case of one participant, me, to check out the structure.
I did not change any code to save the data with this way.
"""