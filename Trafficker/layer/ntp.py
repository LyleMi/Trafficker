import time
import socket
import struct
import datetime

from Trafficker.layer.layer import layer


def _frac(timestamp, n=32):
    return int(abs(timestamp - int(timestamp)) * 2**n)


def _time(intger, frac, n=32):
    return intger + float(frac) / 2**n


class NTP(layer):

    ntpformat = "!BBBb11I"
    JAN_1970 = 2208988800

    def __init__(self, ntp=None):
        # leap second indicator
        self.leap = 0
        # version
        self.version = 2
        # mode
        self.mode = 3
        # stratum
        self.stratum = 0
        # poll interval
        self.poll = 0
        # precision
        self.precision = 0
        # root delay
        self.root_delay = 0
        # root dispersion
        self.root_dispersion = 0
        # reference clock identifier
        self.ref_id = 0
        # reference timestamp
        self.ref_timestamp = 0
        # originate timestamp
        self.orig_timestamp = 0
        self.orig_timestamp_high = 0
        self.orig_timestamp_low = 0
        # receive timestamp
        self.recv_timestamp = 0
        # tansmit timestamp
        self.tx_timestamp = 0
        self.tx_timestamp_high = 0
        self.tx_timestamp_low = 0
        self.keyid = 0
        self.auth = ''

    def pack(self):
        packet = struct.pack(
            self.ntpformat,
            (self.leap << 6 | self.version << 3 | self.mode),
            self.stratum,
            self.poll,
            self.precision,
            int(self.root_delay) << 16 | _frac(self.root_delay, 16),
            int(self.root_dispersion) << 16 | _frac(self.root_dispersion, 16),
            self.ref_id,
            int(self.ref_timestamp),
            _frac(self.ref_timestamp),
            self.orig_timestamp_high,
            self.orig_timestamp_low,
            int(self.recv_timestamp),
            _frac(self.recv_timestamp),
            int(self.tx_timestamp),
            _frac(self.tx_timestamp)
        )
        if self.keyid != 0:
            self.packet += struct.packet('!L', self.keyid)
            self.packet += self.auth
        return packet

    @classmethod
    def unpack(cls, packet):
        unpacked = packet.unpack(cls.ntpformat)
        n = NTP()
        n.leap = unpacked[0] >> 6 & 0x3
        n.version = unpacked[0] >> 3 & 0x7
        n.mode = unpacked[0] & 0x7
        n.stratum = unpacked[1]
        n.poll = unpacked[2]
        n.precision = unpacked[3]
        n.root_delay = float(unpacked[4]) / 2**16
        n.root_dispersion = float(unpacked[5]) / 2**16
        n.ref_id = unpacked[6]
        n.ref_timestamp = _time(unpacked[7], unpacked[8])
        n.orig_timestamp = _time(unpacked[9], unpacked[10])
        n.orig_timestamp_high = unpacked[9]
        n.orig_timestamp_low = unpacked[10]
        n.recv_timestamp = _time(unpacked[11], unpacked[12])
        n.tx_timestamp = _time(unpacked[13], unpacked[14])
        n.tx_timestamp_high = unpacked[13]
        n.tx_timestamp_low = unpacked[14]
        if packet.remaining() > 0:
            n.keyid = packet.unpack('!L')[0]
            n.auth = packet.getremain()
        else:
            n.keyid = ''
            n.auth = b''
        __import__('pprint').pprint(n.json())
        return n

    def json(self):
        # notice ctime is local time, not utc
        def jan1970(timestamp):
            if timestamp != 0.0:
                return timestamp - self.JAN_1970
            else:
                return timestamp
        return {
            "leap": self.leap,
            "version": self.version,
            "mode": self.mode,
            "root_delay": self.root_delay,
            "root_dispersion": self.root_dispersion,
            "ref_id": socket.inet_ntoa(struct.pack('I',socket.htonl(self.ref_id))),
            "ref_timestamp": time.ctime(jan1970(self.ref_timestamp)),
            "recv_timestamp": time.ctime(jan1970(self.recv_timestamp)),
            "tx_timestamp": time.ctime(jan1970(self.tx_timestamp)),
            "keyid": self.keyid,
            "auth": self.auth.hex(),
        }

if __name__ == '__main__':
    n = NTP()
    NTP.unpack(n.pack())
