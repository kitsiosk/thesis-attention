import os
import glob

file = open('noisy.txt', 'r')
# Images list with blank lines separating participants
initial_images = file.readlines()
# Images list without blank lines
images = []

for image in initial_images:
    if image == '\n':
        continue
    images.append(image)
print(len(images))

for i in range(len(images)):
    prefix = images[i].split('/')[1].split('_')[0]
    path = 'dataset/' + prefix + '/' + images[i]
    # Remove the new line character
    path = path[0:-1]
    
    if(os.path.exists(path)):
        os.remove(path)