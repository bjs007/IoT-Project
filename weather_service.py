import urllib
import json
import ConfigParser
from ConfigParser import SafeConfigParser


# by Saurabh Tiwari and Bijay Sharma
# Listen on port 2947 (gpsd) of localhost
# The code parses the json object returned from webservice.
# After parsing we get the city name.
def convert_to_farenheit(temp_in_k):
    return (temp_in_k*9/5.0)-459.67

parser = SafeConfigParser()
parser.read('context.ini')

weather_service_key = parser.get("KeyContext", "weather_service_key")
city_name = parser.get("SecondaryContext", "city")
serviceurl = 'http://api.openweathermap.org/data/2.5/weather?'
url = serviceurl +'q='+ str(city_name) +'&appid='+ str(weather_service_key)
#print url
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(str(data))

temperature = info["main"]["temp"]
pressure = info["main"]["pressure"]
humidity = info["main"]["humidity"]
temp_min = info["main"]["temp_min"]
temp_max = info["main"]["temp_max"]
wind_speed = info["wind"]["speed"]
wind_direction = info["wind"]["deg"]

temperature_f = convert_to_farenheit(temperature)
temp_min_f = convert_to_farenheit(temp_min)
temp_max_f = convert_to_farenheit(temp_max)

parser.set("TertiaryContext", "temperature", str(temperature_f))
parser.set("TertiaryContext", "pressure", str(pressure))
parser.set("TertiaryContext", "humidity", str(humidity))
parser.set("TertiaryContext", "temp_min", str(temp_min_f))
parser.set("TertiaryContext", "temp_max", str(temp_max_f))
parser.set("TertiaryContext", "wind_speed", str(wind_speed))
parser.set("TertiaryContext", "wind_direction", str(wind_direction))

with open('context.ini', 'wb') as configfile:
    parser.write(configfile)
