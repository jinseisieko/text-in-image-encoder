import os
import random
import string

# os.system('touch tests/test3.txt')

ln = 0
for root, dirs, files in os.walk("tests"):
        for file_name in files:
            if file_name.startswith('test'):
                name = file_name.split('.')[0]
                nn = int(name[4:])
                ln = max(ln, nn)

def get_color_contrast_noise(contrast_factor):
    return f"""
def color_contrast_noise(image, contrast_factor={contrast_factor}):
    img_array = np.array(image)
    img_array = (img_array - 128) * contrast_factor + 128
    img_array = np.clip(img_array, 0, 255)
    noisy_img = Image.fromarray(img_array.astype(np.uint8))
    return noisy_img
    """

n_color_contrast_noise = """
def color_contrast_noise(image):
    return image
"""

def get_gaussian_noise(mean, sigma):
    return f"""
def gaussian_noise(image, mean={mean}, sigma={sigma}):
    img_array = np.array(image)
    noise = np.random.normal(mean, sigma, img_array.shape).astype(np.int32)
    noisy_img_array = img_array + noise
    noisy_img_array = np.clip(noisy_img_array, 0, 255)
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img
"""

n_gaussian_noise = """
def gaussian_noise(image):
    return image
"""

def get_salt_and_pepper_noise(amount):
    return f"""
def salt_and_pepper_noise(image, amount={amount}):
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
"""

n_salt_and_pepper_noise = """
def salt_and_pepper_noise(image):
    return image
"""


def get_apply_ludicrous_noise():
    return f"""
def apply_ludicrous_noise(image):
    img = image.convert('L')
    pixels = img.load()
    size = img.size
    for y in range(size[1]):
        for x in range(size[0]):
            original = pixels[x, y]
            if random.random() < 0.5:
                modified = 255 - original
            else:
                noise = random.randint(-128, 128)
                modified = max(0, min(255, original + noise))  # обрезка к [0, 255]

            pixels[x, y] = modified
    return img
"""

n_apply_ludicrous_noise = """
def apply_ludicrous_noise(image):
    return image
"""

n = ln + 1

file = """
def f(image: Image) -> Image:
    image = color_contrast_noise(image)
    image = gaussian_noise(image)
    image = salt_and_pepper_noise(image)
    image = apply_ludicrous_noise(image)
    return image
"""
if input("Do you want color_contrast_noise:") == "Y":
    contrast_factor = float(input("contrast_factor:"))
    file = "\n"+get_color_contrast_noise(contrast_factor)+"\n"+file
else:
    file = "\n"+n_color_contrast_noise+"\n"+file

if input("Do you want gaussian_noise:") == "Y":
    mean = int(input("mean:"))
    sigma = int(input("sigma:"))
    file = "\n"+get_gaussian_noise(mean, sigma)+"\n"+file
else:
    file = "\n"+n_gaussian_noise+"\n"+file

if input("Do you want salt_and_pepper_noise:") == "Y":
    amount = float(input("amount:"))
    file = "\n"+get_salt_and_pepper_noise(amount)+"\n"+file
else:
    file = "\n"+n_salt_and_pepper_noise+"\n"+file

if input("Do you want apply_ludicrous_noise:") == "Y":
    file = "\n"+get_apply_ludicrous_noise()+"\n"+file
else:
    file = "\n"+n_apply_ludicrous_noise+"\n"+file

number = int(input("number:"))
description = input("description:")
file = "\n"+f'description = "{description}"'+"\n"+file

imp = """
import numpy as np
from PIL import Image
import random
"""

file = imp+'\n'+file

os.system(f'touch tests/test{n}.txt')
os.system(f'touch tests/test{n}.py')

with open(f"tests/test{n}.py",'w') as f:
    f.write(file)

with open(f"tests/test{n}.txt", 'w') as f:
    f.write(''.join([random.choice(string.ascii_lowercase+string.digits) for _ in range(number)]))



