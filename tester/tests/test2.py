import numpy as np
from PIL import Image

description = "213, gaussian_noise(0 25)"

def f(image: Image, mean=0, sigma=25) -> Image:
    img_array = np.array(image)
    noise = np.random.normal(mean, sigma, img_array.shape).astype(np.int32)
    noisy_img_array = img_array + noise
    noisy_img_array = np.clip(noisy_img_array, 0, 255)
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img
