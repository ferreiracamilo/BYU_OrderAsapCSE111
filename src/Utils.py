import re, os, shutil

def validate_email(myvalue):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,myvalue):
            return True
        return False

def walk(top):
    directory = None
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            directory = os.path.join(root, name)
        for name in files:
            f1 = os.path.join(root, name)
            if f1.endswith('.pdf') and directory:
                shutil.move(f1,top+"\\Invoices")
    #walk(os.path.realpath(os.curdir))