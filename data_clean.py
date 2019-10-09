import json

with open('data.json') as json_file:
    noisy_data = json.load(json_file)

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

print(len(noisy_data))
for i in range(len(images)):
    prefix = images[i].split('/')[1].split('_')[0]
    path = prefix + '/' + images[i]
    # Remove the new line character
    path = path[0:-1]
    ret = noisy_data.pop(path, None)
    # if ret == None:
    #     print(path)
# Data is not noisy anymore
print(len(noisy_data))

with open('data_cleaned.json', 'w') as json_file:
    json.dump(noisy_data, json_file)