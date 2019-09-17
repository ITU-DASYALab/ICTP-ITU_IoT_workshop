# test Temperature and humidity sensor (Si7006-A20)
# https://www.silabs.com/documents/public/data-sheets/Si7006-A20.pdf
#
from pysense import Pysense
from SI7006A20 import SI7006A20
import pycom
import micropython
import machine
import time

pycom.heartbeat(False)
py = Pysense()
tempHum = SI7006A20(py)
while True:
    temperature = tempHum.temp()
    humidity = tempHum.humidity()
    if temperature < 35:
        pycom.rgbled(0x007f00)
    elif temperature > 35:
        pycom.rgbled(0x7f0000)
    print("Temperature: {} Degrees  Humidity: {}".format(temperature, humidity))
    time.sleep(1)
