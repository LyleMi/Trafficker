#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


class layer(object):

    """base layer"""

    def __init__(self, packet=""):
        self.packet = packet

    def pack(self):
        return self.packet

    def __str__(self):
        return self.pack()

    def __repr__(self):
        return "<%s>" % self.name

    @property
    def name(self):
        return self.__class__.__name__

    @staticmethod
    def send(layers, port=0, device="eth0"):
        packet = ''.join([p.pack() for p in layers])
        if len(packet) < 60:
            packet += "\x00" * (60 - len(packet))
        self.hexdump(packet)
        return "=== TEST ==="
        rawSocket = socket.socket(
            socket.PF_PACKET, socket.SOCK_RAW, socket.htons(port)
        )
        rawSocket.bind((device, socket.htons(port)))
        rawSocket.send(packet)
        return rawSocket

    @staticmethod
    def calChecksum(data):
        s = 0
        n = len(data) % 2
        for i in range(0, len(data)-n, 2):
            s += data[i] + (data[i+1] << 8)
        if n:
            s += data[i+1]
        while (s >> 16):
            s = (s & 0xFFFF) + (s >> 16)
        s = ~s & 0xffff
        return s

    @staticmethod
    def hexdump(src, length=16, show=True):
        result = []
        digits = 4 if isinstance(src, unicode) else 2

        for i in xrange(0, len(src), length):
            s = src[i:i+length]
            hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
            text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
            result.append(b"%04X   %-*s   %s" %
                          (i, length*(digits + 1), hexa, text))

        if show:
            print(b'\n'.join(result))
        else:
            return b'\n'.join(result)

    @staticmethod
    def parseMac(s, encode=False):
        if encode:
            s = s.hex()
            tmp = []
            for i in range(len(s)//2):
                tmp.append(s[i*2:(i+1)*2])
            return ":".join(tmp)
        return bytes.fromhex(s.replace(':', ''))
