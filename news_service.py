import urllib
import json
import ConfigParser
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('context.ini')

news_service_key = parser.get("KeyContext", "news_service_key")
city_name = parser.get("SecondaryContext", "city")
news_item = 10

serviceurl = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
url = serviceurl +'q='+ str(city_name) +'&api-key='+ str(news_service_key)
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(str(data))

n_parser = SafeConfigParser()
n_parser.add_section("NewsItems")

for i in range (news_item):
        n_parser.set("NewsItems", str("web_url: "+ str(i)), str(info["response"]["docs"][i]["web_url"]))
        print str(info["response"]["docs"][i]["lead_paragraph"])
        print i


with open('news.ini', 'wb') as configfile:
    n_parser.write(configfile)
