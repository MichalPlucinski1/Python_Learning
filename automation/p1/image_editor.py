from PIL import Image, ImageEnhance, ImageFilter
import os

path = './automation/p1/imgs'
pathOut = '/automation/p1/editedImgs'


print(os.listdir(path))

for filename in os.listdir(path):
    img = Image.open(f"{path}\\{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    new_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}\\{new_name}_edited.png')

