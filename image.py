from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

scale = "   .,-~:;=!*#$@"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def get_density(val):
    tmp = round(val / (255 / len(scale)))
    return scale[tmp]

image_path = 'pfp.png' 
image = Image.open(image_path)

newsize = (50, 50)
image = image.resize(newsize)

# Convert image to a numpy
image_array = np.array(image)

height, width, channels = image_array.shape

image_array = rgb2gray(image_array)
# Loop through each pixel and invert the colors
# for i in range(height):
#     for j in range(width):
#         r, g, b = image_array[i][j]
#         print(r, g, b)
        
# Convert the numpy array back to an image
image = Image.fromarray(image_array)

# Display the image using matplotlib
plt.imshow(image)
plt.axis('off')
plt.show()

for i in range(height):
    row = ""
    for j in range(width):
        row += get_density(image_array[i][j])
    print(row)