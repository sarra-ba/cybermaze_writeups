import os, zlib, string

obj_dir = r"C:\Users\lenovo\Downloads\vault\.git\objects"

def printable(s):  
    return ''.join(c for c in s if c in string.printable)

for root, _, files in os.walk(obj_dir):
    for f in files:
        path = os.path.join(root, f)
        try:
            data = zlib.decompress(open(path,"rb").read())
            txt = printable(data.decode(errors="ignore"))
            if len(txt.strip()) > 5:  # ignore empty content
                print("\n==== OBJECT ====\n", txt)
        except:
            pass
