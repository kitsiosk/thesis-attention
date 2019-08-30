# Attention Measurement/ Data Collection Procedure

*Prerequisites*: All packages installed are documented in requirements.txt

The main idea is to show users two types of screens and ask them to hit Space upon looking them:
* A white screen with a black dot at a random point, where the user must look at the dot and hit Space
* A white screen with text instructing the user to look away from the screen and then hit Space

The key press then triggers the webcam to capture a frame at that very moment and save it in format
UUID_x_y.jpg. The frame is saved either in directory dataset/UUID/positives or dataset/UUID/negatives depending on wether the user was looking inside or outside the screen.

The python file to implement the above is main.py. The attention point on the screen is represented by a circle of center (x, y) and side 2*R where x and y are randomly chosen between the screen boundaries and R is a hyperparameter. The functionality of main.py can be summarized as follows:
* Initialize screen dimensions
* Define the number of frames to capture from each user NUM_OF_FRAMES and the length of the rectangle R
* Input from user his/her age, gender and laptop used
* For i=0...NUM_OF_FRAMES
  * Randomly initialize the circle center (x, y) and color it black
  * Ask user to press Space key according to where they focus their attention as defined above
  * Capture a frame of the user at the moment the key is pressed and save it. 

## To run the program:
* git clone this project
* install all packages in requirements.txt with pip
* create an empty folder 'dataset'
* run main.py


Contact me for any corrections/questions: Kitsios Konstantinos