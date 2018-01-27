# Trafficker

[![Python 2.7](https://img.shields.io/badge/Python-2.7-blue.svg)](http://www.python.org/download/)

A tool used to send arbitrary packet or parse pcap packet.

## Installation

> only support Linux momentarily

```shell
pip install -r requirements.txt
git clone https://github.com/LyleMi/Trafficker.git
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
from packets.pcap import Pcap
Pcap("./pcaps/test.pcap")
```