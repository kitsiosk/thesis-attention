import numpy as np
import cv2
import glob, os, json

NUM_OF_FRAMES = 5

# Load the dataset
with open('data.json') as json_file:
    data = json.load(json_file)

# Extract the keys in sorted order
keys = sorted(data)
indexes = np.random.randint(len(keys), size=NUM_OF_FRAMES)

message = input('Hello! You are about to see {} number of frames with human faces taken from a \
laptop camera. We need you to guess if the person \
is looking inside the laptop screen or outside. If your guess \
is inside, press \'l\', else press \'n\'. When you are ready press Enter to start'.format(NUM_OF_FRAMES))

# Initialize values for True Positive, True Negative, False Positive
# and False Negative to zeros
tp, tn, fp, fn = 0, 0, 0, 0

for i in range(NUM_OF_FRAMES):
    key = keys[indexes[i]]
    # Extract the groundtruth
    y = key.split('/')[1]

    im = cv2.imread('dataset_new/' + key)
    cv2.imshow(y, im)
    ans = cv2.waitKey(0)
    cv2.destroyAllWindows()

    # True positive
    if(ans == ord('l') and y == 'positive'):
        tp += 1
    # True negative
    elif(ans == ord('n') and y == 'negative'):
        tn += 1
    # False positive
    elif(ans == ord('l') and y == 'negative'):
        fp += 1
    # False negative
    elif(ans == ord('n') and y == 'positive'):
        fn += 1

accuracy = float(tp + tn)/(tp + tn + fp + fn)
precision = float(tp)/(tp + fp)
recall = float(tp)/(tp + fn)
f1_score = float(2*precision*recall)/(precision + recall)

print('Accuracy: ', accuracy)
print('Precision: ',  precision)
print('Recall: ', recall)
print('F1 Score: ', f1_score)