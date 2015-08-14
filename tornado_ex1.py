import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello ,world")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("user_info.html")
    def post(self):
        self.render("hello.html",name = self.get_argument("name"))
application = tornado.web.Application([
    (r"/",MainHandler),
    (r"/hello/",HelloHandler)
,])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
