My SI7021 sensor class using SMBus2 package for RaspberryPi.

When I bought the SI7021 Adafruit sensor [SI7021 Adafruit sensor](https://www.adafruit.com/product/3251)
I originally struggled to read the sensor over the I2C bus using the standard SMbus library included with Python.
After hours of trawling forums the general consensus was to do a double byte read with SMBus. When I did this however,
I noticed that both bytes received were always identical. Most people may not have even noticed this because when
you carry out the maths needed to turn the byte data into temperature and humidity (as shown in the datasheet) it would 
mask that the bytes were the same.

I came across a library called [SMBus2](https://github.com/kplindegaard/smbus2) which allowed me to create a read/write
message with a 'repeated start' which is whats required for the I2C communication with the SI7021. This was absolutely
fantastic! I was now getting different 2 byes in the returned word. And when I did the math conversion shown in the SI7021 
datasheet, the temperature and humidity were bang on!

A side note is I think the pigpio library enables this feature but at the time I didnt understand threads and daemons 
particularly well so I wanted a little more control myself.

I've added a test case to the git repo showing how to use the code.