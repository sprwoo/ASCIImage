# Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import math

# Constants
DENSITIES = "  .'`^\",:;Il!i><~+_-?][}{1)(|\\/#MW&8%B@$"
RESIZE = (100, 100)
NTSC_CONST = np.array([0.2989, 0.587, 0.114])

def NTSC_formula(rgb):
    return np.dot(rgb, NTSC_CONST.T)

def density_character(val):
    tmp = math.floor(val / (255 / len(DENSITIES)))
    return DENSITIES[tmp]

def convert_to_ascii(image_array):
    row = ""
    for i in range(height):
        for j in range(width):
            pixel = NTSC_formula(image_array[i][j][:3])
            row += density_character(pixel)
        row += "\n"
    return row

def show_image(image):
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    image_path = 'am.jpg' 
    image = Image.open(image_path)
    image = image.resize(RESIZE)
    # show_image(image)

    # Convert image to a numpy
    image_array = np.array(image)
    height, width, channels = image_array.shape
    ascii_image = convert_to_ascii(image_array)

    root = tk.Tk()
    root.geometry("500x700")
    root.title("Window")

    print(ascii_image)
    window = tk.Label(root, text=ascii_image, anchor='w', justify='left', font=('Courier New', 14), highlightthickness=0, borderwidth=0, pady=0)
    window.pack()

    root.mainloop()

    image.close()


