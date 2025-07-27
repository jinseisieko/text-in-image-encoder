
import numpy as np
from PIL import Image
import random


description = "1000, salt_and_pepper_noise(0.05)"


def apply_ludicrous_noise(image):
    return image



def salt_and_pepper_noise(image, amount=0.05):
    img_array = np.array(image)
    total_pixels = img_array.size
    num_salt = int(amount * total_pixels / 2)
    num_pepper = int(amount * total_pixels / 2)
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in img_array.shape]
    img_array[salt_coords[0], salt_coords[1]] = 255
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in img_array.shape]
    img_array[pepper_coords[0], pepper_coords[1]] = 0
    noisy_img = Image.fromarray(img_array)
    return noisy_img



def gaussian_noise(image):
    return image



def color_contrast_noise(image):
    return image


def f(image: Image) -> Image:
    image = color_contrast_noise(image)
    image = gaussian_noise(image)
    image = salt_and_pepper_noise(image)
    image = apply_ludicrous_noise(image)
    return image
