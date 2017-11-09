#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads

import tornado.web

from layer.mac import ETHER
from layer.ip import IP
from layer.layer import layer

class IPHandler(tornado.web.RequestHandler):

    def post(self):
        mac_config = loads(self.get_argument('mac'))
        ip_config  = loads(self.get_argument('ip'))
        # print mac_config, ip_config
        mac = ETHER(mac_config)
        ip = IP(ip_config)
        s = layer.send([mac, ip])
        print s
        # print s.recv(4096)
