import paho.mqtt.client as mqtt
import random
import time
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
while True:
    temp = random.randint(60, 90)
    client.publish("plant/pumps", f'{{"device": "pump_01", "temp": {temp}}}')
    time.sleep(1)
client.disconnect()