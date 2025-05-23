from PIL import Image
filename = '3.jpg.webp'
with Image.open(filename) as img:
    width, height = img.size
    resized_img = img.resize((width // 3, height // 3))
    resized_img.save('resized_image.jpg')

    horizontal_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal_mirror.save('horizontal_mirror.jpg')

    vertical_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
    vertical_mirror.save('vertical_mirror.jpg')
