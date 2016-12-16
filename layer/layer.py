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
    def send(layers, port = 0):
        packet = ''.join([p.pack() for p in layers])
        if len(packet) < 60:
            packet += "\x00" * (60 - len(packet))
        hexdump(packet)
        return "=== TEST ==="
        rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(port))
        rawSocket.bind(("eth0",socket.htons(port)))
        rawSocket.send(packet) 
        return rawSocket