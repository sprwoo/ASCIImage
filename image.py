# Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Constants
DENSITIES = "   .,-~:;=!*#$@"
RESIZE = (50, 50)
NTSC_CONST = np.array([0.2989, 0.587, 0.114])

def NTSC_formula(rgb):
    return np.dot(rgb, NTSC_CONST.T)

def density_character(val):
    tmp = round(val / (255 / len(DENSITIES)))
    return DENSITIES[tmp]

def convert_to_ascii(image_array):
    for i in range(height):
        row = ""
        for j in range(width):
            pixel = NTSC_formula(image_array[i][j][:3])
            row += density_character(pixel)
        print(row)

def show_image(image):
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    image_path = 'pfp.png' 
    image = Image.open(image_path)
    image = image.resize(RESIZE)
    show_image(image)

    # Convert image to a numpy
    image_array = np.array(image)
    height, width, channels = image_array.shape
    convert_to_ascii(image_array)

    image.close()



