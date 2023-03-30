import re

def validate_email(myvalue):
        #Local function
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,myvalue):
            return True
        return False