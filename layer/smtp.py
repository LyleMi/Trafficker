#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from layer import layer


class SMTPParseError(Exception):
    pass

class SMTP(layer):

    def __init__(self):
        pass

    def pack(self):
        pass

    @staticmethod
    def unpack(packet):
        if len(packet) <= 0:
            return None
        if not packet.endswith("\r\n"):
            raise SMTPParseError("error terminator")
            return None
        s = SMTP()
        s.content = packet
        return s

if __name__ == '__main__':
    pass
