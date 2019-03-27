# Trafficker

[![Python 3.6](https://img.shields.io/badge/Python-2.7-bule.svg)](http://www.python.org/download/)

任意流量发包，pcap解析工具

## 安装

```shell
git clone https://github.com/LyleMi/Trafficker.git
python setup.py install
```

## 特性

### 支持协议

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

### 使用

```python
from Trafficker.packets.pcap import Pcap
p = Pcap("./pcaps/test.pcap")
for packetNumber, p in p.parse():
    print(packetNumber, p, p.json())
```

或

```python
from Trafficker.packets.pcap import Pcap
from Trafficker.handlers.tcp import tcpHandler
p = Pcap("./pcaps/test.pcap")
pcap.parseWithCallback([tcpHandler])
```
