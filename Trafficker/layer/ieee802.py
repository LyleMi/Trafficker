#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

from Trafficker.layer.layer import layer


class IEEE802dot3(layer):

    # 802.3
    # Todo
    etypes = {
        "STP": 0x4242
    }
