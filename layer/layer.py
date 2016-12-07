import socket

from utils.utils import hexdump

class layer(object):
    """docstring for layer"""
    def __init__(self):
        self.packet = ""

    def pack(self):
        return ''

    def __str__(self):
        return self.pack()

    @staticmethod
    def send(layers, dst):
        packet = ''.join([l.pack() for l in layers])
        hexdump(packet)
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_RAW)
        s.sendto(packet, (dst, 0))
        return s