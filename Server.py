__version__ = "0.1"

import shutil

""" This is just a dummy code for server """


class SimpleHTTPRequestHandler():
    aws_user = None
    aws_password = None
    s3_bucket = None
    region = None

    server_version = "SimpleHTTP/" + __version__

    def do_GET(self):
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def copyfile(self, source, outputfile):
        """connect to aws s3 load file content and serve it to client """
        shutil.copyfileobj(source, outputfile)


if __name__ == '__main__':
    port = 8080
    server = BaseHTTPServer.HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    server.serve_forever()
