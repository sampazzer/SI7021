from mySI7021 import temp_humid

th_sensor = temp_humid()

th_sensor.humidity_temp_set()

my_humidity = th_sensor.humidity_get()

my_temperature = th_sensor.temp_get()

print("humid: {}, temp: {}".format(my_humidity, my_temperature))