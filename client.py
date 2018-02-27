import paho.mqtt.client as mqtt
from colorama import Fore,Back,Style
import random

random.seed()

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]


class user:
    def __init__(self):
        self.name = raw_input("enter your name to start : ")
        self.color = colors[random.randint(0,len(colors)-1)]

        self.send("entered the room")

    def send(self,message):
        client = mqtt.Client(self.name+"12")
        client.username_pw_set("lujanoih","8i0lJO9t9_km")
        client.connect("m23.cloudmqtt.com", 19625,20)

        msg = Style.BRIGHT + self.color + self.name
        msg = msg + Style.DIM +" : "+ Style.RESET_ALL
        msg = msg + self.color + message + Fore.RESET + Style.RESET_ALL

        client.publish("timepass-mqtt", msg)


wanderer = user()

while True:
    print "message : ",
    message = raw_input()
    wanderer.send(message)

