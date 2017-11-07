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

    # pcap文件包头解析
    pcapHeader = {}
    pcapHeader['magic_number'] = data[0:4]
    pcapHeader['version_major'] = data[4:6]
    pcapHeader['version_minor'] = data[6:8]
    pcapHeader['thiszone'] = data[8:12]
    pcapHeader['sigfigs'] = data[12:16]
    pcapHeader['snaplen'] = data[16:20]
    pcapHeader['linktype'] = data[20:24]

    # pcap文件的数据包解析
    step = 0
    packetNum = 0

    packetHeader = {}

    while True:

        data = fpcap.read(16)
        if len(data) < 16:
            break

        # 数据包头各个字段
        packetHeader['GMTtime'] = data[:4]
        packetHeader['MicroTime'] = data[4:8]
        packetHeader['caplen'] = data[8:12]
        packetHeader['len'] = data[12:16]
        # 求出此包的包长len
        packetLen = struct.unpack('I', packetHeader['len'])[0]
        # 写入此包数据
        tmp = fpcap.read(packetLen)
        mac = ETHER.unpack(tmp[:14])

        html.write("<hr />")
        html.write("src mac: %s," % mac[0].encode("hex").upper())
        html.write("dst mac: %s," % mac[1].encode("hex").upper())

        if mac[2] == 2048:
            html.write("Type: IPv4")
            ip = IP.unpack(tmp[14:34])

            html.write("<br />")
            html.write("%s -> %s" % (ip[-2], ip[-1]))

            if ip[-3] == 1:
                html.write(" Type: ICMP")
            elif ip[-3] == 2:
                html.write(" Type: IGMP")
            elif ip[-3] == 6:
                html.write(" Type: TCP")
            elif ip[-3] == 17:
                html.write(" Type: UDP")

        elif mac[2] == 2054:
            html.write("Type: ARP")
        elif mac[2] == 34525:
            html.write("Type: IPv6")

        html.write("<br /><pre>")
        html.write(escape(hexdump(tmp, 16, False)))
        html.write("</pre>")
        packetNum += 1

    html.write(htmlfooter)

    fpcap.close()
    html.close()

if __name__ == '__main__':
    parsePcap("./static/pcaps/test.pcap", "./static/pcaps/test.html")
