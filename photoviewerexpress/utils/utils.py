import os
import Image

def get_image_parms(path):
    img = Image.open(path)
    pic_format = img.format.lower()
    w, h = img.size
    ratio = 800.0/max(w, h)
    if ratio < 1:
        img = img.resize((int(w*ratio), int(h*ratio)), Image.ANTIALIAS)

    return img.save, pic_format

def get_thumb_parms(path):
    size = 300, 300
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    return img.save, img.format.lower()

def scan_dir(path):
    formats = (".jpg", ".jpeg", ".git", ".png")
    return ([f for f in os.listdir(path)
             if os.path.isdir(os.path.join(path,f))],
            [f for f in os.listdir(path) if (
                os.path.isfile(os.path.join(path,f))
                and os.path.splitext(f)[1].lower() in formats
                )])

