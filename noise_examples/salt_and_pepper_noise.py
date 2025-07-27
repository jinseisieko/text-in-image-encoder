import numpy as np
from PIL import Image

def salt_and_pepper_noise(image, amount=0.05):
    # Преобразуем изображение в массив numpy
    img_array = np.array(image)
    
    # Вычисляем количество пикселей, которые нужно изменить
    total_pixels = img_array.size
    num_salt = int(amount * total_pixels / 2)
    num_pepper = int(amount * total_pixels / 2)

    # Добавляем "соль" (белые пиксели)
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in img_array.shape]
    img_array[salt_coords[0], salt_coords[1]] = 255

    # Добавляем "перец" (черные пиксели)
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in img_array.shape]
    img_array[pepper_coords[0], pepper_coords[1]] = 0

    # Преобразуем массив обратно в изображение
    noisy_img = Image.fromarray(img_array)
    return noisy_img

img = Image.open('input_image.png')
noisy_img = salt_and_pepper_noise(img)
noisy_img.show()
