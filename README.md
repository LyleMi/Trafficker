# Trafficker

[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](http://www.python.org/download/)

A tool used to send arbitrary packet or parse pcap packet.

## Installation

> only support Linux momentarily

```shell
git clone https://github.com/LyleMi/Trafficker.git
python setup.py install
```

## Feature

### Suppoerted Protocol

* arp
* dns
* icmp
* igmp
* ip
* pop
* smtp
* tcp
* udp
* vlan

### Usage

```python
from Trafficker.packets.pcap import Pcap
p = Pcap("./pcaps/test.pcap")
for packetNumber, p in p.parse():
    print(packetNumber, p, p.json())
```

or

```python
from Trafficker.packets.pcap import Pcap
from Trafficker.handlers.tcp import tcpHandler
p = Pcap("./pcaps/test.pcap")
pcap.parseWithCallback([tcpHandler])
```
