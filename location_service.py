#!/usr/bin/env python
import urllib
import json
from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read('context.ini')
lati = parser.get("PrimaryContext", "latitude")
longi = parser.get("PrimaryContext", "longitude")
geo_key = parser.get("KeyContext", "geolocation_key")

# by Saurabh Tiwari and Bijay Sharma
# Listen on port 2947 (gpsd) of localhost
# The code parses the json object returned from webservice.
# After parsing we get the city name.


serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
url = serviceurl +lati+','+longi+'&key='+geo_key
#print url
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(str(data))
city = info["results"][0]["address_components"][3]["long_name"]
parser.set("SecondaryContext", "city", city)
with open('context.ini','wb') as configfile:
	parser.write(configfile)
