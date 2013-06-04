import os


def scan_dir(path):
    formats = (".jpg", ".jpeg", ".git", ".png")
    return ([f for f in os.listdir(path) 
             if os.path.isdir(os.path.join(path,f))],
            [f for f in os.listdir(path) if (
                os.path.isfile(os.path.join(path,f)) 
                and os.path.splitext(f)[1].lower() in formats
                )])

def check_mini(dirname, filenames):
    missing = []
    if not os.path.exists(os.path.join(dirname, ".mini")):
        return filenames
    for f in filenames:
        if not os.path.exists(os.path.join(dirname, ".mini", f)):
            missing.append(f)
    return missing

def create_mini(dirname, filenames):
    minidir = os.path.join(dirname, ".mini")
    if not os.path.exists(os.path.join(dirname, ".mini")):
        os.mkdir(minidir)
    for f in filenames:
        print "creating", os.path.join(minidir, f)
        fd = open(os.path.join(minidir, f), "w")
        fd.write(f)
        fd.close()
                 
    
        
              

if __name__ == "__main__":
    import sys
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]

    dirname, files = scan_dir(path)
    missing = check_mini(path, files)
    print "Missing: ", missing
    create_mini(path, missing)
    
