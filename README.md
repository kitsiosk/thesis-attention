# Attention Measurement/ Data Collection Procedure

*Prerequisites*: All packages installed are documented in requirements.txt

The main idea is to show users a number of white screens with a black point in a random position inside the screen and ask them to press one of two keys:
* 'L' key, if they are looking to the point at the time they hit the key
* 'N' key, if they are looking to any other point at the time they hit the key

The key press then triggers the webcam to capture a frame at that very moment and save it in format
UUID_x_y.jpg. The frame is saved either in directory dataset/UUID/positives or dataset/UUID/negatives depending on wether the user pressed 'L' or 'N'.

The python file to implement the above is main.py. The attention point on the screen is represented by a circle of center (x, y) and side 2*R where x and y are randomly chosen between the screen boundaries and R is a hyperparameter. The functionality of main.py can be summarized as follows:
* Initialize screen dimensions by taking a screenshot and saving its shape
* Define the number of frames to capture from each user NUM_OF_FRAMES and the length of the rectangle R
* Input from user his/her age, gender
* For i=0...NUM_OF_FRAMES
  * Randomly initialize the rectangle center (x, y) and color it black
  * Ask user to press 'L' key or 'N' key according to where they focus their attention
  * Capture a frame of the user at the moment the key is pressed and save it. 

## To run the program:
* git clone this project
* install all packages in requirements.txt with pip
* create an empty folder 'dataset'
* run main.py


Contact me for any corrections/questions: Kitsios Konstantinos