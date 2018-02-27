import paho.mqtt.client as paho

broker = "m23.cloudmqtt.com"

def on_connect(client,userdata,qos,rc):
    client.subscribe("timepass-mqtt")

def on_message(client,userdata,msg):
    print str(msg.payload)

client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("lujanoih","8i0lJO9t9_km")
client.connect("m23.cloudmqtt.com",19625,60)

client.loop_forever()
