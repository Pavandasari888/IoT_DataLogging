import json
import paho.mqtt.client as mqtt
import datetime
now = datetime.datetime.now()

from datetime import datetime

def pumpfun(pump):

    date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        pump_dict = json.loads(pump)
        if "temp" not in pump_dict:
            error_message = f"{date_string}| ERROR : Missing temperature data"
            print(error_message)
            with open("pump_log.txt", "a") as file:
                file.write(error_message + "\n")
            return 
                
        if pump_dict["temp"] > 80:
            status = "ALERT: Temperature critical"
        else:
            status = "Temperature normal"

        log_message = (
            f"{date_string} | "
            f"Device: {pump_dict['device']} | "
            f"Temp: {pump_dict['temp']} | "
            f"{status}"
        )

        print(log_message)

        with open("pump_log.txt", "a") as file:
            file.write(log_message + "\n")

    except json.JSONDecodeError:
        error_message = f"{date_string}| ERROR : Invalid JSON format"
        print(error_message)
        with open("pump_log.txt", "a") as file:
            file.write(error_message + "\n")
            
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    pumpfun(payload)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("localhost", 1883);
client.subscribe("plant/pumps")
client.loop_forever()

