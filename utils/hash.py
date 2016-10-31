import hashlib

def md5(s):
    return hashlib.md5(str(s)).hexdigest()
