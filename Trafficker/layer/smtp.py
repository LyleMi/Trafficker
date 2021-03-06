import socket
import struct

from Trafficker.layer.layer import layer


class SMTPParseError(Exception):
    pass


class SMTP(layer):

    cmds = ['auth', 'ehlo', 'mail', 'rcrt', 'helo',
            'quit', 'rset', 'data', 'bdat', 'user',
            'pass', 'list', 'uidl', 'capa']
    codes = ['221', '220', '250', '334', '354', '550']

    def __init__(self, rawdata=b''):
        self.errorno = 0
        self.type = ''
        self.rawdata = rawdata

    def pack(self):
        return self.rawdata

    @classmethod
    def unpack(cls, packet):
        s = SMTP()
        s.rawdata = packet
        if len(packet) < 1:
            s.type = 'null'
            return s
        if len(packet) > 100:
            s.type = 'bigdata'
            s.data = packet
            return s
        p = str(packet).split('\r\n')
        fp = p[0].split(' ')
        if fp[0] in cls.codes:
            s.type = 'ret'
            s.code = fp[0]
            if len(p) > 1:
                s.msg = fp[1:]
        elif fp[0].lower() in cls.cmds:
            s.type = 'req'
            s.cmd = fp[0]
            if len(p) > 1:
                s.args = fp[1:]
        return s

    def __repr__(self):
        return "<SMTP %s>" % self.type

if __name__ == '__main__':
    pass
