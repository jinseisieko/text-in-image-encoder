
import numpy as np
from PIL import Image
import random


description = "600, gaussian_noise(0 20), salt_and_pepper_noise(0.04)"


def apply_ludicrous_noise(image):
    return image



def salt_and_pepper_noise(image, amount=0.04):
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



def gaussian_noise(image, mean=0, sigma=20):
    img_array = np.array(image)
    noise = np.random.normal(mean, sigma, img_array.shape).astype(np.int32)
    noisy_img_array = img_array + noise
    noisy_img_array = np.clip(noisy_img_array, 0, 255)
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img



def color_contrast_noise(image):
    return image


def f(image: Image) -> Image:
    image = color_contrast_noise(image)
    image = gaussian_noise(image)
    image = salt_and_pepper_noise(image)
    image = apply_ludicrous_noise(image)
    return image
