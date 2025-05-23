from PIL import Image
import os

# Имя файла с водяным знаком (обязательно должно быть в формате png!)
WATERMARK_FILE = 'watermark.webp'

# Директория с исходными изображениями
SOURCE_DIRECTORY = 'D:\аип\lab 9\filtered_images'

# Директория вывода результатов
DESTINATION_DIRECTORY = 'D:\аип\lab 9\watermarked'

# Создать папку назначения, если она отсутствует
if not os.path.exists(DESTINATION_DIRECTORY):
    os.makedirs(DESTINATION_DIRECTORY)

# Загрузка водяного знака
watermark = Image.open(WATERMARK_FILE)

# Перебираем все файлы в директории SOURCE_DIRECTORY
for filename in os.listdir(SOURCE_DIRECTORY):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        source_image_path = os.path.join(SOURCE_DIRECTORY, filename)

        # Открытие исходного изображения
        base_image = Image.open(source_image_path)

        # Настройка размера водяного знака (~10% от ширины оригинала)
        width_percentage = 0.1  # процент от ширины изображения
        wsize = int(base_image.width * width_percentage)
        hsize = int(watermark.height * (wsize / float(watermark.width)))
        resized_watermark = watermark.resize((wsize, hsize), Image.Resampling.LANCZOS)

        # Определяем положение водяного знака (центр внизу справа)
        pos_x = base_image.width - resized_watermark.width - 10
        pos_y = base_image.height - resized_watermark.height - 10

        # Создание копии исходного изображения с поддержкой альфа-канала
        rgba_base_image = base_image.convert("RGBA")

        # Наложение водяного знака
        rgba_base_image.paste(resized_watermark, (pos_x, pos_y), resized_watermark)

        # Формирование нового пути сохранения результата
        dest_image_path = os.path.join(DESTINATION_DIRECTORY, filename)

        # Сохранение финального изображения
        rgba_base_image.save(dest_image_path)

print("Водяные знаки были успешно добавлены.")
