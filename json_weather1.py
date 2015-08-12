import urllib.request

url = "http://api.openweathermap.org/data/2.5/forecast/daily?cnt=7&units=meteric&mode=json&q=London"

req = urllib.request.Request(url)
#forecast_string = urllib.request.urlopen(req).read()
#forecast_dict = json.loads(forecast_string.decode("UTF-8"))
print(urllib.request.urlopen(req).read())

#print(forecast_dict)
