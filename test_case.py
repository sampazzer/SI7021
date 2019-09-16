#SI7021 In Use#

from mySI7021 import temp_humid

#define the class
my_sensor = temp_humid()

#tell the sensor to make a humidity and temperature read
my_sensor.humidity_temp_set()

#store the read values to your own variables
#values are returned as int rounded to 2 decimal places
my_humidity = my_sensor.humidity_get()

my_temperature = my_sensor.temp_get()

#print values to stdout
print("Humidity: {}, Temperature: {}".format(my_humidity, my_temperature))
