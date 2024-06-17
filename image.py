from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = 'daniel.jpg' 
image = Image.open(image_path)

# Convert image to a numpy
image_array = np.array(image)
print(image_array)

height, width, channels = image_array.shape

# Loop through each pixel and invert the colors
for i in range(height):
    for j in range(width):
        r, g, b = image_array[i, j]

# Convert the numpy array back to an image
back = Image.fromarray(image_array)

# Display the image using matplotlib
plt.imshow(back)
plt.axis('off')
plt.show()
