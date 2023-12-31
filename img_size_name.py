# python (location)\img_size_name.py
# change size & name --> All img (jpg, JPG, JPEG) from the folder

from PIL import Image
import os
from datetime import datetime

PATH_IMGS = '.../images//'
PATH_IMGS_RESIZED = '.../images-Resized//'


def resize():
    for image_file_name in os.listdir(PATH_IMGS):
        if image_file_name.endswith((".jpg", ".JPG", ".JPEG")):
            new_file_name = datetime.now().strftime('%f')

            im = Image.open(PATH_IMGS +image_file_name)
            new_height = 1000
            new_width  = int(new_height / im.height * im.width)
            im = im.resize((new_width, new_height), Image.LANCZOS)
            im.save(PATH_IMGS_RESIZED + new_file_name + '-NEW_NAME' + '.jpg')


if __name__ == "__main__":
    resize()