#sudo apt-get install python3-w1thermsensor

from w1thermsensor import W1ThermSensor
from time import sleep

sensor = W1ThermSensor()
temperature_in_celsius = sensor.get_temperature()
temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)

print("Temperature is %s" % temperature_in_fahrenheit)
