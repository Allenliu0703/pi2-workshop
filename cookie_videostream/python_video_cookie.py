import tornado.ioloop
import tornado.web
import datetime
import time
import subprocess
import picamera

users = {"Allen":"910703","Doris":"930901"}

class ImageHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self,patch):
         self.set_header('Cache-Control','no-store,no-cache,must-revalidate,'+
                         ' max-age=0')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        print(self.get_argument("name"))
        print(self.get_argument("password"))
        #if self.get_argument("name") in users.keys() and users[self.get_argument("name")] == self.get_argument("password"):
        if self.get_argument("name") in users.keys() and users[self.get_argument("name")] == self.get_argument("password"):
            self.set_secure_cookie("user",self.get_argument("name"))
            self.redirect("/video")
        else :
            self.render("logfail.html")

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user")
        self.render("logout.html")

class VideoHandler (tornado.web.RequestHandler):
    
    def get(self):
        if not self.get_secure_cookie("user"):
            self.redirect("/login")
            return
        subprocess.call(["raspistill","-w","200","-h","200",
                         "-e","jpg","-n","-t","1","-o","/home/pi/images/live.jpg"])
        self.render("video.html")
    def post(self):
        if self.get_argument("left")=="turnleft" and self.get_argument("right") != "turnright":
            print(1)
            x = self.get_argument("right") 
        else:
            x = self.get_argument("left")   
        if self.get_argument("right")=="turnright":
            print(2)
        else:
            y = self.get_argument("right")
        
        


class AllenHandler (tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie("user"):
            self.redirect("/login")
            return
        delta = datetime.datetime(2016,5,30)-datetime.datetime.now()
        remainingdays = delta.days
        remaininghours = delta.seconds//3600
        remainingminutes = delta.seconds//60 - remaininghours*60
        self.render("allen&doris.html",days = remainingdays, hours = remaininghours, minutes = remainingminutes)

application = tornado.web.Application([
    (r"/login",LoginHandler),
    (r"/video",VideoHandler),
    (r"/logout",LogoutHandler),
    (r"/allen&doris",AllenHandler),
    (r"/images/(.*)",ImageHandler, {"path":"/home/pi/images"})],
    cookie_secret= 'allenlovedoris')

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
            
            
