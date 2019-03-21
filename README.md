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
* ip
* pop
* smtp
* tcp
* udp
* vlan

### Usage

```python
from Trafficker.packets.pcap import Pcap
Pcap("./pcaps/test.pcap")
```
