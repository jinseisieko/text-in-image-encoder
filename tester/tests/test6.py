
import numpy as np
from PIL import Image
import random


description = "500, color_contrast_noise(0.4), gaussian_noise(0 25)"


def apply_ludicrous_noise(image):
    return image



def salt_and_pepper_noise(image):
    return image



def gaussian_noise(image, mean=0, sigma=25):
    img_array = np.array(image)
    noise = np.random.normal(mean, sigma, img_array.shape).astype(np.int32)
    noisy_img_array = img_array + noise
    noisy_img_array = np.clip(noisy_img_array, 0, 255)
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img



def color_contrast_noise(image, contrast_factor=0.4):
    img_array = np.array(image)
    img_array = (img_array - 128) * contrast_factor + 128
    img_array = np.clip(img_array, 0, 255)
    noisy_img = Image.fromarray(img_array.astype(np.uint8))
    return noisy_img
    

def f(image: Image) -> Image:
    image = color_contrast_noise(image)
    image = gaussian_noise(image)
    image = salt_and_pepper_noise(image)
    image = apply_ludicrous_noise(image)
    return image
