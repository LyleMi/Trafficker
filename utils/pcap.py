# coding=utf-8

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
    <link href="/static/css/lib/bootstrap.min.css" rel="stylesheet">
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

    string_data = fpcap.read()

    # pcap文件包头解析
    pcap_header = {}
    pcap_header['magic_number'] = string_data[0:4]
    pcap_header['version_major'] = string_data[4:6]
    pcap_header['version_minor'] = string_data[6:8]
    pcap_header['thiszone'] = string_data[8:12]
    pcap_header['sigfigs'] = string_data[12:16]
    pcap_header['snaplen'] = string_data[16:20]
    pcap_header['linktype'] = string_data[20:24]

    # pcap文件的数据包解析
    step = 0
    packet_num = 0
    packet_data = []

    pcap_packet_header = {}
    i = 24

    while(i < len(string_data)):

        # 数据包头各个字段
        pcap_packet_header['GMTtime'] = string_data[i:i+4]
        pcap_packet_header['MicroTime'] = string_data[i+4:i+8]
        pcap_packet_header['caplen'] = string_data[i+8:i+12]
        pcap_packet_header['len'] = string_data[i+12:i+16]
        # 求出此包的包长len
        packet_len = struct.unpack('I', pcap_packet_header['len'])[0]
        # 写入此包数据
        tmp = string_data[i+16:i+16+packet_len]
        mac = ETHER.unpack(tmp[:14])

        html.write("<hr />")
        html.write("src mac: " + mac[0].encode("hex").upper() + ", ")
        html.write("dst mac: " + mac[1].encode("hex").upper() + ", ")

        if mac[2] == 2048:
            html.write("Type: IPv4")
            ip = IP.unpack(tmp[14:34])

            html.write("<br />")
            html.write(ip[-2] + " -> " + ip[-1])
            
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
        i = i + packet_len+16
        packet_num += 1

    html.write(htmlfooter)


    fpcap.close()
    html.close()
