import tornado.ioloop
import tornado.web
import urllib.request, json
6
class CityHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("city_info.html")
    def post(self):
        url = "http://api.openweathermap.org/data/2.5/forecast/daily?cnt=7&units=meteric&mode=json&q="+self.get_argument("city")
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        self.forecast = json.loads(response.read().decode("UTF-8"))
        self.render("weather_forecast.html",city_name = self.get_argument("city"), forecast = self.forecast['list'])

application = tornado.web.Application([
    (r"/weatherforecast/",CityHandler)
,])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
