from ledstrip import LEDStrip
import time
import random
#import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder
import json
import requests
from threading import Thread

CLK = 3
DAT = 2

strip = LEDStrip(CLK, DAT)

server_url = "ws://192.168.0.18:86/ColorHub"
username = "BRIAN_RPI"

hub_connection = HubConnectionBuilder()\
    .with_url(server_url)\
    .with_automatic_reconnect({
        "type": "raw",
        "keep_alive_interval": 10,
        "reconnect_interval": 5,
        "max_attempts": 5
    }).build()
    
def colorChanger2(color):
	r = color["red"]
	b = color["blue"]
	g = color["green"]
	print(r)
	strip.setcolourrgb(r, g, b)

def colorChanger(message):
	color = json.loads(''.join(message))
	print("Json String")
	print(color)
	r = color["red"]
	b = color["blue"]
	g = color["green"]
	print(r)
	strip.setcolourrgb(r, g, b)
	
def startUp():
	for ra in range(50, 200):
		r = random.randint(0, 255)
		b = random.randint(0, 255)
		g = random.randint(0, 255)
		strip.setcolourrgb(r, g, b)
		time.sleep(0.10)
	strip.setcolourrgb(100, 45, 124)
	
def reconnect():
    print("connection closed")
    time.sleep(20)
    print("try reconnect")
    hub_connection.start()

def signalrStarter():
	hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
	hub_connection.on_close(lambda: reconnect)

	print("Connecting to hub")
	hub_connection.on("sendColor", colorChanger)

	hub_connection.start()
	startUp()
	print("Connected to hub")
	#while True:
		#print("Shite")
	message = input("Press any button to quit")
	hub_connection.stop()
	print("Exiting")
	sys.exit(0)
	
def getLastColor():
	URL = "http://192.168.0.18:86/api/Colors/getlatestcolor"
	r = requests.get(url = URL)
	data = r.json()
	print(data)
	colorChanger2(data)
	
if __name__ == "__main__":
	tStartup = Thread(target = startUp, args = ())
	tGetLastColor = Thread(target = getLastColor, args = ())
	tStartSignalr = Thread(target = signalrStarter, args = ())
	tStartup.start()
	tStartup.join()
	tGetLastColor.start()
	tGetLastColor.join()
	tStartSignalr.start()
	tStartSignalr.join()
	
	

