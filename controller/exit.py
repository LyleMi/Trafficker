import tornado.web

class exitHandler(tornado.web.RequestHandler):

    def get(self):
        tornado.ioloop.IOLoop.instance().stop()