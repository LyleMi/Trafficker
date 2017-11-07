#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
from cgi import escape
from json import dumps

from utils import hexdump
from layer.mac import ETHER
from layer.ip import IP


htmlheader = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Parse Result</title>
    <link href="../css/lib/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
<h1>PCAP Parse Result</h1>

'''

htmlfooter = '''
</div>
</body>
</html>
'''


def parsePcap(pcapfile, distFile):

    fpcap = open(pcapfile, 'rb')
    html = open(distFile, 'w')
    html.write(htmlheader)

    data = fpcap.read(24)
    packetNum = 0

    while True:

        data = fpcap.read(16)
        if len(data) < 16:
            break

        packetLen = struct.unpack('I', data[12:16])[0]
        tmp = fpcap.read(packetLen)
        mac = ETHER.unpack(tmp[:14])

        html.write("<hr />")
        html.write("src mac: %s," % mac.src.encode("hex").upper())
        html.write("dst mac: %s," % mac.dst.encode("hex").upper())
        html.write("Type: %s" % mac.stype)

        if mac.type == mac.IPv4:

            ip = IP.unpack(tmp[14:34])

            html.write("<br />")
            html.write("%s => %s" % (ip[-2], ip[-1]))

            if ip[-3] == 1:
                html.write(" Type: ICMP")
            elif ip[-3] == 2:
                html.write(" Type: IGMP")
            elif ip[-3] == 6:
                html.write(" Type: TCP")
            elif ip[-3] == 17:
                html.write(" Type: UDP")

        html.write("<br /><pre>")
        html.write(escape(hexdump(tmp, 16, False)))
        html.write("</pre>")
        packetNum += 1

    html.write(htmlfooter)

    fpcap.close()
    html.close()


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(".."))
    parsePcap("./static/pcaps/test.pcap", "./static/pcaps/test.html")
