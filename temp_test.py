#This adds my SI7021 class and returns the temperature and humidity to the console

from mySI7021 import temp_humid

#Create my sensor object.
th_sensor = temp_humid()

#Carries out the I2C data transaction.
th_sensor.humidity_temp_set()

#Gets the humidity value. It is an int rounded to 2 decimal places.
my_humidity = th_sensor.humidity_get()

#Gets the temperature value. It is an int rounded to 2 decimal places.
my_temperature = th_sensor.temp_get()

#Prints the results in the terminal.
print("humid: {}, temp: {}".format(my_humidity, my_temperature))
