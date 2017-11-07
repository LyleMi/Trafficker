#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import dpkt
import tornado.web

from utils.utils import md5
from utils.pcap import parsePcap

upload_path = os.path.split(os.path.dirname(__file__))[0]
upload_path = os.path.join(upload_path, 'static', 'pcaps')


class PCAPHandler(tornado.web.RequestHandler):

    def get(self):
        x = list(os.listdir(upload_path))
        # print x
        x = filter(lambda i: i.endswith(".html"), x)
        self.write(json.dumps(x))

    def post(self):

        file_metas = self.request.files['file']
        filename = md5(file_metas[0]['body'])
        filepath = os.path.join(upload_path, filename)
        for meta in file_metas:
            with open(filepath + '.pcap', 'wb') as up:
                up.write(meta['body'])
        parsePcap(filepath + '.pcap', filepath + '.html')
        self.redirect('/#/pcap')