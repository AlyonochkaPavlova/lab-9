from PIL import Image
img_path = '1.jpg.webp'
try:
    img = Image.open(img_path)
except FileNotFoundError:
    print("Файл изображения не найден.")
    exit()
img.show()
width, height = img.size
format = img.format
mode = img.mode

print(f"\nИнформация о файле:\nРазмер изображения: {width}x{height}\nФормат файла: {format}\nЦветовая модель: {mode}")
