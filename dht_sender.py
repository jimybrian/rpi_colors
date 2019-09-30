import Adafruit_DHT
import requests
import time
from threading import Thread

sensor = Adafruit_DHT.DHT11
pin = 17


def sendData(h, t):
	URL = "http://167.99.88.230:5000/api/Readings/addReading"
	data = {"temperature":t, "humidity":h}
	print(data)
	r = requests.post(url = URL, json = data, verify=False)
	print(r.status_code)
	print(r.text)
	print("Data Sent")
	
def readSensor():
	h, t = Adafruit_DHT.read_retry(sensor, pin)
	print("Humidity")
	print(h)
	print("Temperature")
	print(t)
	sendData(h, t)
	
if __name__ == "__main__":
	while True:
		readSensor()	
		time.sleep(300)
	
