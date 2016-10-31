import os
import tornado.web

from utils.hash import md5

upload_path = os.path.split(os.path.dirname(__file__))[0]
upload_path = os.path.join(upload_path, 'uploads')


class PCAPHandler(tornado.web.RequestHandler):

    def post(self):

        file_metas = self.request.files['file']
        filename = md5(file_metas[0]['body'])
        for meta in file_metas:
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
        self.write('finished!')
