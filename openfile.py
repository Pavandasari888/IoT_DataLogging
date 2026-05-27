import json
import paho.mqtt.client as mqtt
import datetime

now = datetime.datetime.now()

def pumpfun(pump):
    pump_dict = json.loads(pump)
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    if pump_dict["temp"] > 80:
        status = "Alert:Temperature critical"
    else:
        status = "temperature normal"
        log_message=f"{date_string} | Device: {pump_dict['device']} | Temp: {pump_dict['temp']} | {status}"
        print(log_message)
        with open("pump_log.txt", "a") as file:
            file.write(log_message + "\n")
            
            
