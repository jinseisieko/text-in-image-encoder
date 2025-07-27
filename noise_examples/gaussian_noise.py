import numpy as np
from PIL import Image

def gaussian_noise(image, mean=0, sigma=25):
    img_array = np.array(image)
    
    # Генерация шума (среднее значение и стандартное отклонение)
    noise = np.random.normal(mean, sigma, img_array.shape).astype(np.int32)
    
    # Добавление шума к изображению
    noisy_img_array = img_array + noise
    
    # Ограничиваем значения пикселей от 0 до 255
    noisy_img_array = np.clip(noisy_img_array, 0, 255)
    
    # Преобразуем массив обратно в изображение
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img

img = Image.open('input_image.png')
noisy_img = gaussian_noise(img)
noisy_img.show()
