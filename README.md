#Attention Measurement
##Data Collection Procedure

*Prerequisites*: All packages installed are documented in requirements.txt

The main idea is to show users a number of white screens with a black point in a random position inside the screen and ask them to press one of two keys:
* Up key, if they are looking to the point at the time they hit the key
* Down key, if they are looking to any other point at the time they hit the key

The key press then triggers the webcam to capture a frame at that very moment and save it in format
UUID_x_y.jpg. The frame is saved either in directory dataset/positives or dataset/negatives depending on wether the user pressed up key or down key.

The python file to implement the above is main.py. The attention point on the screen is represented by a rectangle of center (x, y) and side 2*R where x and y are randomly chosen between the screen boundaries and R is a hyperparameter. The functionality of main.py can be summarized as follows:
* Initialize screen dimensions by taking a screenshot and saving its shape
* Define the number of frames to capture from each user NUM_OF_FRAMES and the length of the rectangle R
* Input from user his/her age, gender
* For i=0...NUM_OF_FRAMES
  *Randomly initialize the rectangle center (x, y) and color it black
  *Ask user to press up key or down key according to where they focus their attention
  *Capture a frame of the user at the moment the key is pressed and save it. 




Contact me for any corrections/questions: Kitsios Konstantinos