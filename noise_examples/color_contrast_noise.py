import numpy as np
from PIL import Image

def color_contrast_noise(image, contrast_factor=0.5):
    img_array = np.array(image)
    
    # Применяем коэффициент контраста
    img_array = (img_array - 128) * contrast_factor + 128
    
    # Ограничиваем значения пикселей от 0 до 255
    img_array = np.clip(img_array, 0, 255)
    
    # Преобразуем массив обратно в изображение
    noisy_img = Image.fromarray(img_array.astype(np.uint8))
    return noisy_img

img = Image.open('input_image.png')
noisy_img = color_contrast_noise(img)
noisy_img.show()
