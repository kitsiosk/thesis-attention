import numpy as np
import cv2
import pyscreenshot as ImageGrab
from imutils.video import VideoStream

# Video caption
cap = VideoStream(src=0).start()

# Boolean that is true when user's attention is on the given point
# and false otherwise
attention = False

# Number of frames to save each time the program runs
NUM_OF_FRAMES = 3

# Take a screenshot to calculate screen res. It is saved in Pillow format
screenshot = ImageGrab.grab()
# Convert it to opencv format
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# Save the screen height and width
HEIGHT = screenshot.shape[0] 
WIDTH = screenshot.shape[1]
R = 10

print('You will see 3 consequtive white screens with a black point somewhere. We need you to press either the upkey or the downkey at each screen depending on wether you are looking at the black point directly(then press the upkey at that very moment) or looking at any other point of the screen (then press the downkey at that very moment).')
input('When you are ready, press enter to start!')

i=0
while i < NUM_OF_FRAMES:
    # Initialize a white screen
    screen = np.ones((HEIGHT, WIDTH))

    # Choose a random point on the screen
    x = np.random.randint(R, WIDTH-R)
    y = np.random.randint(R, HEIGHT-R)

    # Color black the rectangle of side 2R and center the point (x, y)
    screen[y-R:y+R, x-R:x+R] = 0

    cv2.imshow('screen', screen)
    ans = cv2.waitKey(0)

    frame = cap.read()

    # 82 is the integer value for 'up' key
    # 84 is the integer value for 'down' key
    if ans == 82:
        attention = True
        i=i+1
    elif ans == 84:
        attention = False
        i=i+1
    else:
        print('You must press either upkey or downkey')
    
    cv2.imwrite('dataset/' + str(i) + '.jpg', frame)
    print(ans)
    print(x)
    print(y)
    print(attention)

# When everything is done, release the capture
cap.stop()
cv2.destroyAllWindows()