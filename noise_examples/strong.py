import random

from PIL import Image


def apply_ludicrous_noise(input_path, output_path):
    """
    Применяет сильный шум к изображению:
    - С вероятностью 50% инвертирует пиксель.
    - Иначе добавляет случайный шум в диапазоне [-128, 128].
    """
    img = Image.open(input_path).convert('L')  # серое изображение
    pixels = img.load()
    size = img.size

    for y in range(size[1]):
        for x in range(size[0]):
            original = pixels[x, y]

            if random.random() < 0.5:
                modified = 255 - original  # инвертировать
            else:
                noise = random.randint(-128, 128)
                modified = max(0, min(255, original + noise))  # обрезка к [0, 255]

            pixels[x, y] = modified

    img.save(output_path)
    print(f"Saved noisy image to: {output_path}")


if __name__ == "__main__":
    apply_ludicrous_noise('v4.png', 'v5.png')
