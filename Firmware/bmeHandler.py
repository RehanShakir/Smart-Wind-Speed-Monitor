import bme280
import smbus2
from time import sleep

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)
def getBME280Data():
    global bus,address,port
    bme280_data = bme280.sample(bus,address)
    #print("Humidity ; Pressure ; Temperature")
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    #print(humidity, pressure, ambient_temperature)
    #sleep(1)
    return [humidity,pressure,ambient_temperature]