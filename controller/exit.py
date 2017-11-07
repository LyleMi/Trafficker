#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class exitHandler(tornado.web.RequestHandler):

    def get(self):
        tornado.ioloop.IOLoop.instance().stop()