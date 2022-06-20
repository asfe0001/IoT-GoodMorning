import requests
import json
import math
import paho.mqtt.client as mqtt
import time


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
        #get weather Data
        rawdata = get_weather(apiKey,city)

        #write relevant data into json
        weather1 = json.dumps({
            "temp"  :   math.trunc(rawdata["main"]["temp"] - 273.15),
            "hum": math.trunc(rawdata["main"]["humidity"]),
            "sky": rawdata["weather"][0]["description"]
        },indent = 4)


        # Publish
        client.publish("weather", weather1)
        print("Sent weather message\t", weather1)
        time.sleep(20)

    except KeyboardInterrupt:
        break

