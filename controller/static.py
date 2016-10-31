import tornado.web

class StaticFile(tornado.web.StaticFileHandler):  
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")