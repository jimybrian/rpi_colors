import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder

def writeMessage(message):
    print(message)

server_url = "ws://192.168.0.18:86/ColorHub"
username = "BRIAN_RPI"

hub_connection = HubConnectionBuilder()\
    .with_url(server_url)\
    .configure_logging(logging.DEBUG)\
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
hub_connection.on("SendColor", writeMessage)
hub_connection.start()
print("Connected to hub")
message = input(">> ")
#
#message = None
#while message != "exit()":
#    message = input(">> ")
#    if message is not None and message is not "" and message is not "exit()":
#        hub_connection.send("SendColor", [username, message])
#
#hub_connection.stop()

sys.exit(0)
