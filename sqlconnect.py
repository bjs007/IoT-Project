import MySQLdb
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('context.ini')

#[KeyContext]
geolocation_key = str(parser.get("KeyContext", "geolocation_key"))
weather_service_key = str(parser.get("KeyContext", "weather_service_key"))

#[PrimaryContext]
latitude = str(parser.get("PrimaryContext", "latitude"))
longitude = str(parser.get("PrimaryContext", "longitude"))

#[SecondaryContext]
city = str(parser.get("SecondaryContext", "city"))

#[TertiaryContext]
temperature = str(parser.get("TertiaryContext", "temperature"))
pressure = str(parser.get("TertiaryContext", "pressure"))
humidity = str(parser.get("TertiaryContext", "humidity"))
temp_min = str(parser.get("TertiaryContext", "temp_min"))
temp_max = str(parser.get("TertiaryContext", "temp_max"))
wind_speed = str(parser.get("TertiaryContext", "wind_speed"))
wind_direction = str(parser.get("TertiaryContext", "wind_direction"))

#[ContextReason]
room_temperature_preference = str(parser.get("ContextReason", "room_temperature_preference"))
heating_unit_on = str(parser.get("ContextReason", "heating_unit_on"))
cooling_unit_on = str(parser.get("ContextReason", "cooling_unit_on"))
heating_unit_t_difference = str(parser.get("ContextReason", "heating_unit_t_difference"))
cooling_unit_t_difference = str(parser.get("ContextReason", "cooling_unit_t_difference"))


conn = MySQLdb.connect(host= "stiwari5-cluster.cluster-cltssb30vxlo.us-east-1.rds.amazonaws.com",
                  user="ta_user",
                  passwd="welcome1",
                  db="tourist_assist")
x = conn.cursor()

try:
   x.execute("""INSERT INTO context_aware_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(geolocation_key, weather_service_key, latitude, longitude, city, temperature, pressure, humidity, temp_min, temp_max, wind_speed, wind_direction, room_temperature_preference, heating_unit_on, cooling_unit_on, heating_unit_t_difference, cooling_unit_t_difference))
   conn.commit()
   print "Data Inserted Successfully into mysql TABLE " + context_aware_data
   print "Hostname: stiwari5-cluster.cluster-cltssb30vxlo.us-east-1.rds.amazonaws.com"
except:
   conn.rollback()
   print "Data insertion failed"

conn.close()
