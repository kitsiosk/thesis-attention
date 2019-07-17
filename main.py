import numpy as np
import cv2

cap = cv2.VideoCapture(0)

HEIGHT = 500
WIDTH  = 800
R = 5

# Initialize a white screen
screen = np.ones((500, 800))

# Choose a random point on the screen
x = np.random.randint(WIDTH)
y = np.random.randint(HEIGHT)

# Color black the rectangle of side 2R and center the point (x, y)
screen[y-R:y+R, x-R:x+R] = 0

# cv2.imshow('screen', screen)
# cv2.waitKey(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
    
#     if ret == True:
#         # Display the resulting frame
#         cv2.imshow('frame',frame)

#         # Press 'q' to exit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()