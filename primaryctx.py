import gps
from sys import argv
from decimal import *
import ConfigParser

# The code has been partially derived from the raspberry pi tutorial
# And supporting documents of adafruit
# The part that averages things and file read write has been authored
# by Saurabh Tiwari and Bijay Sharma
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
experiment_count = 10
average_lat = 0;
average_lon = 0;
num_times = 0

while (experiment_count > 0):
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
		if report['class'] == 'TPV':
			if hasattr(report, 'lat'):
				print "latitude = ", report.lat
				average_lat += Decimal(report.lat)
			if hasattr(report, 'lon'):
				print "longitude = ", report.lon
				average_lon += Decimal(report.lon)
				num_times += 1
				experiment_count -= 1
				print "experiment_count", experiment_count
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print ("GPSD has terminated")
average_lat = average_lat/num_times
average_lon = average_lon/num_times

cfgfile = open("context.ini", 'w')

config = ConfigParser.ConfigParser()
config.add_section('PrimaryContext')
config.set('PrimaryContext', 'latitude', average_lat)
config.set('PrimaryContext','longitude', average_lon)
config.write(cfgfile)
cfgfile.close()
