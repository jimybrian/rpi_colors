import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

print("Humidity")
print(humidity)
print("Temperature")
print(temperature)
