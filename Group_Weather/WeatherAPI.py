import requests
import json
import math
import paho.mqtt.client as mqtt
import time
from datetime import datetime

# MQTT Broker User Variables
username = "ubuntu"
password = "ubuntu"
adress = "983072be-6928-4aa5-94db-b538ea35100f.ka.bw-cloud-instance.org"    # Broker URLs

# Connect to mqtt broker
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(adress, 1883, 60)

# Weather
apiKey = "ad60e179c345ea260ea7541f6baf33a9"
city = "Karlsruhe"
def get_weather(pApiKey, pCity):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={pCity}&appid={pApiKey}"
    return requests.get(url).json()


while(1):
    try:
        rawdata = get_weather(apiKey,city)      # get weather Data


        #print(json.dumps(rawdata, indent = 4, sort_keys=True))     # Original Json File from API

        """
            print("Current Temperature: " + str(math.trunc(rawdata["main"]["temp"] - 273.15)) + "°C")
            print("Current Humidity: " + str(math.trunc(rawdata["main"]["humidity"])) + " %")
            print("Suntime: " + str(round((rawdata["sys"]["sunset"] - rawdata["sys"]["sunrise"])/3600 ,1)) + " h")
            print("Current Air Pressure: " + str(rawdata["main"]["pressure"]) + " Pa")
            print("Clouds: " + str(rawdata["weather"][0]["description"]))
            print("Current Time: " + str(time.strftime("%H:%M:%S")))
            print("Sunrise: " + str(datetime.utcfromtimestamp(rawdata["sys"]["sunrise"]+timezone).strftime('%H:%M:%S')))
            print("Sunset: " + str(datetime.utcfromtimestamp(rawdata["sys"]["sunset"]+timezone).strftime('%H:%M:%S')))
            """
        weather = json.dumps({                      # Json file with relevant data
            "temp"  :   math.trunc(rawdata["main"]["temp"] - 273.15),
            "press" :   rawdata["main"]["pressure"],
            "hum"   :   math.trunc(rawdata["main"]["humidity"]),
            "stime" :   round((rawdata["sys"]["sunset"] - rawdata["sys"]["sunrise"])/3600 ,1),
            "sky"   :   rawdata["weather"][0]["description"],
            "time"  :   time.strftime("%H:%M:%S"),
            "rise"  :   datetime.utcfromtimestamp(rawdata["sys"]["sunrise"]+rawdata["timezone"]).strftime('%H:%M:%S'),
            "set"   :   datetime.utcfromtimestamp(rawdata["sys"]["sunset"]+rawdata["timezone"]).strftime('%H:%M:%S')
            },indent = 4)


        #print(weather)

        # Publish
        client.publish("weather", weather)
        print("Sent weather message\t", weather)
        time.sleep(3)

    except KeyboardInterrupt:
        break

