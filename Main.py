from os import system
from ConfigParser import SafeConfigParser
import datetime
import time

parser = SafeConfigParser()
parser.read("log.ini")

system('python location_service.py')
system('python weather_service.py')
system('python temperature_controller.py')
#system('python news_service.py')

ts = time.time()
ts = datetime.datetime.fromtimestamp(ts).strftime('%m-%d-%y %H:%M:%S')
parser.set("run_timestamp", "time", str(ts))
with open('log.ini','wb') as configfile:
	parser.write(configfile)
