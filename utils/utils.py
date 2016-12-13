import socket
import hashlib

def md5(s):
    return hashlib.md5(str(s)).hexdigest()


def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data)-n, 2):
        s += ord(data[i]) + (ord(data[i+1]) << 8)
    if n:
        s += ord(data[i+1])
    while (s >> 16):
        # print("s >> 16: ", s >> 16)
        s = (s & 0xFFFF) + (s >> 16)
    # print("sum:", s)
    s = ~s & 0xffff
    return s


def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append(b"%04X   %-*s   %s" %
                      (i, length*(digits + 1), hexa, text))

    print b'\n'.join(result)


def parseMac(s):
    return s.replace(':', '').decode('hex')
