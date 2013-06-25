import os
import Image

def get_image_parms(path, res=800):
    img = Image.open(path)
    pic_format = img.format.lower()
    w, h = img.size
    ratio = float(res)/max(w, h)
    if ratio < 1:
        img = img.resize((int(w*ratio), int(h*ratio)), Image.ANTIALIAS)

    return img.save, pic_format

def get_thumb_parms(path, res):
    size = int(res), int(res)
    img = Image.open(path)
    img.thumbnail(size, Image.ANTIALIAS)
    return img.save, img.format.lower()

def scan_root(base, path, include_private=False):
    pbdirs, pbfiles = scan_dir(base, os.path.join(path, "public"),
                               prepend="public")
    if include_private:
        pvdirs, pvfiles = scan_dir(base, os.path.join(path, "private"), 
                                   prepend="private")
        return pbdirs + pvdirs, pbfiles + pvfiles
    return pbdirs, pbfiles

def scan_dir(base, rel_path, prepend="", *args, **kargs):
    prepend = prepend
    path = os.path.join(base, rel_path)
    formats = (".jpg", ".jpeg", ".git", ".png")
    return ([os.path.join(prepend, f) for f in os.listdir(path)
             if os.path.isdir(os.path.join(path,f))],
            [os.path.join(prepend, f) for f in os.listdir(path) if (
                os.path.isfile(os.path.join(path,f))
                and os.path.splitext(f)[1].lower() in formats
                )])

