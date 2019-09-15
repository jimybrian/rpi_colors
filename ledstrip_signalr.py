from ledstrip import LEDStrip
import time
import random
#import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder
import json

CLK = 3
DAT = 2

strip = LEDStrip(CLK, DAT)

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
	r = random.randint(0, 255)
	b = random.randint(0, 255)
	g = random.randint(0, 255)
	strip.setcolourrgb(r, g, b)
	time.sleep(0.50)
    
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

hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
hub_connection.on_close(lambda: reconnect)

def reconnect():
    print("connection closed")
    time.sleep(20)
    print("try reconnect")
    hub_connection.start()

print("Connecting to hub")
hub_connection.on("sendColor", colorChanger)

hub_connection.start()
startUp()
print("Connected to hub")
message = input("Press any button to quit")
hub_connection.stop()
print("Exiting")
sys.exit(0)
	
