import os
from PIL import Image, ImageEnhance
filenames = ['1.jpg.webp', '2.jpg.webp', '3.jpg.webp', '4.jpg.jpg', '5.jpg.jpg']
output_folder = 'filtered_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in filenames:
    try:
        with Image.open(filename) as img:
            enhancer = ImageEnhance.Contrast(img)
            enhanced_img = enhancer.enhance(1.5)
            new_filename = f"{output_folder}{filename.split('.')[0]}_enhanced.jpg"
            enhanced_img.save(new_filename)

        print(f"Успешно обработано изображение {filename}. Новый файл: {new_filename}")

    except Exception as e:
        print(f"Произошла ошибка при обработке файла {filename}: {e}")
