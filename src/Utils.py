import re, os, shutil
from dateutil.parser import parse


def is_email(myvalue):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,myvalue):
            return True
        return False

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def move(top):
    """Move PDF files from project folder to Invoices subfolder

    Args:
        top (_type_): main folder of project, current directory is the same

    You may use the line below to execute it
    move(os.path.realpath(os.curdir))
    """
    directory = None
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            directory = os.path.join(root, name)
        for name in files:
            f1 = os.path.join(root, name)
            if f1.endswith('.pdf') and directory:
                file_name_parent_folder = top+"\\"+name
                if os.path.exists(file_name_parent_folder):
                    shutil.move(f1,top+"\\Invoices")


def remove(top):
    """Remove PDF files from project folder, this is for unit test validation

    Args:
        top (_type_): main folder of project, current directory is the same

    You may use the line below to execute it
    remove(os.path.realpath(os.curdir))
    """
    directory = None
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            directory = os.path.join(root, name)
        for name in files:
            f1 = os.path.join(root, name)
            if f1.endswith('.pdf') and directory:
                file_name = top+"\\"+name
                if os.path.exists(file_name):
                    os.remove(file_name)