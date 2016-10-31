#!/usr/bin/env python
# coding:utf-8
import os
import sys
import webbrowser

import tornado.options
import tornado.ioloop
import tornado.web

import controller.base

tornado.options.define(
    "port", default=8888, help="Run server on a specific port", type=int)
tornado.options.define(
    "host", default="localhost", help="Run server on a specific host")
tornado.options.define("url", default=None, help="Url to show in HTML")
tornado.options.parse_command_line()

if not tornado.options.options.url:
    tornado.options.options.url = "http://%s:%d" % (
        tornado.options.options.host, tornado.options.options.port)

settings = {
    "base_url": tornado.options.options.url,
    "template_path": "static",
    "cookie_secret": "bxzasdgjhas",
    "compress_response": True,
    "default_handler_class": controller.base.NotFoundHandler,
    # "xsrf_cookies": True,
    "static_path": "static",
}

path = os.path.join(os.getcwd(), "web")

handlers = [
    (r"/", "controller.main.MainHandler"),
    (r"/ip", "controller.ip.IPHandler"),
    (r"/exit", "controller.exit.exitHandler"),
    (r'/pcap', "controller.pcap.PCAPHandler"),
]


if __name__ == "__main__":
    try:
        app = tornado.web.Application(handlers, debug=True, **settings)
        print "run at %s" % tornado.options.options.url
        app.listen(tornado.options.options.port)
        webbrowser.open(tornado.options.options.url)
        tornado.ioloop.IOLoop.instance().start()
    except:
        import traceback
        print traceback.print_exc()
    finally:
        sys.exit(0)
