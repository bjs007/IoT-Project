from ConfigParser import SafeConfigParser
from decimal import *

# By Saurabh Tiwari and Bijay Sharma
# Listen on port 2947 (gpsd) of localhost
# The code read the config file and get the weather outside
# It then decides on the basis of RULES (reasoning technique) the temperature of a room

from ConfigParser import SafeConfigParser


parser = SafeConfigParser()
parser.read("context.ini")
curr_temp = Decimal(parser.get("TertiaryContext","temperature"))
room_temp = (parser.get("ContextReason","room_temperature_preference"))

if room_temp is '':
	print "User has not yet set the room temperature preference!!!"
        room_temp = raw_input('Set temperature preference in fahrenheit:')
	parser.set("ContextReason", "room_temperature_preference", room_temp)


room_temp = Decimal(room_temp)


if curr_temp >= room_temp:
	cooling_unit_t_difference = curr_temp - room_temp
	parser.set("ContextReason", "cooling_unit_t_difference", str(cooling_unit_t_difference))
	parser.set("ContextReason", "heating_unit_t_difference", str(0.00))
	parser.set("ContextReason", "heating_unit_on", 'False')
	parser.set("ContextReason", "cooling_unit_on", 'True')
else:
	heating_unit_t_difference = room_temp - curr_temp
	parser.set("ContextReason", "heating_unit_t_difference", str(heating_unit_t_difference))
	parser.set("ContextReason", "cooling_unit_t_difference", str(0.00))
	parser.set("ContextReason", "heating_unit_on", 'True')
	parser.set("ContextReason", "cooling_unit_on", 'False')


with open('context.ini','wb') as configfile:
	parser.write(configfile)
	
		

