# -*- coding: utf-8 -*-
"""
Created on 20.06.2022

@author: Assistent und die Manager
"""

# !usr/bin/python3 #shebang line
import paho.mqtt.client as mqtt  # import paho-mqtt as mqtt client
import json  # import json library
import time

Lichtstaerke = 0  # default
Bewegung = 0   # default
Kaffeestaerke = 0    # default
Temp = 0 # default
Luftfeuchtigkeit = 0 # default
Wolken = 0   # default
broker_address = "983072be-6928-4aa5-94db-b538ea35100f.ka.bw-cloud-instance.org"


Topics = [("Goodmorning/Bett/Bewegung", 0), ("Goodmorning/Licht/Lichtstaerke", 0), ("Goodmorning/Kaffee", 0), ("Goodmorning/weather",0)]
subscriber_dict_Bett = {}
subscriber_dict_Licht = {}
subscriber_dict_Wetter = {}


def pub_Kaffee(Kaffeestaerke):
    publisher_dict = {"Kaffeestaerke: ",Kaffeestaerke}
    publisher_json = json.dumps(publisher_dict)  # convert publisher_dict into json string format
    client.publish("IoTGoodMorning", publisher_json)  # publish message
    print("message published: ", publisher_json)  # print published message



def callback_Licht(client, userdata, message):
    global subscriber_dict_Licht
    global Lichtstaerke

    subscriber_dict_Licht =json.loads(
        str(message.payload.decode("utf-8")))
    print("message received: ", subscriber_dict_Licht)
    Lichtstaerke = subscriber_dict_Licht["Lichtstaerke"]
    print("Lichtstaerke: ", Lichtstaerke)

def callback_Bett(client, userdata, message):
    global subscriber_dict_Bett
    global Bewegung

    subscriber_dict_Bett = json.loads(
        str(message.payload.decode("utf-8")))
    print("message received: ", subscriber_dict_Bett)
    Bewegung = subscriber_dict_Licht["Bewegung"]
    print("Bewegung: ", Bewegung)

def callback_Wetter(client, userdata, message):
    global subscriber_dict_Wetter
    global temp
    global Luftfeuchtigkeit
    global Wolken

    subscriber_dict_Wetter = json.loads(
        str(message.payload.decode("utf-8")))
    print("message received: ", subscriber_dict_Wetter)
    Temp = subscriber_dict_Licht["temp"]
    print("Temperatur: ", temp)
    Luftfeuchtigkeit = subscriber_dict_Wetter["hum"]
    print("Luftfeuchtigkeit: ", Luftfeuchtigkeit)
    Wolken = subscriber_dict_Wetter["sky"]
    print("Wolken: ", Wolken)




broker_address = "983072be-6928-4aa5-94db-b538ea35100f.ka.bw-cloud-instance.org"  # broker adress
client = mqtt.Client("Assistent")  # create new instance
client.message_callback_add("Goodmorning/Bett", callback_Bett)  # attach on_message function to a callback function
client.message_callback_add("Goodmorning/Licht", callback_Licht)  # attach on_message function to a callback function
client.message_callback_add("Goodmorning/Wetter", callback_Wetter)  # attach on_message function to a callback function
client.connect(broker_address)  # connect to broker
client.loop_start()  # start the client loop to make it always running
client.subscribe(Topics)  # subscribe to topic

try:
    while True:
        if (Lichtstaerke > 80):  # hell?
            if(Bewegung < 26):
                pub_Kaffee(2)
            elif(Bewegung > 25 & Bewegung < 51):
                pub_Kaffee(5)
            elif(Bewegung > 50 & Bewegung < 76):
                pub_Kaffee(8)
            elif(Bewegung > 75 & Bewegung <= 100):
                pub_Kaffee(10)
        print(Temp)
        print(Luftfeuchtigkeit)
        print(Wolken)


        time.sleep(3)  # sleep or wait for 3s before continuing to the next loop


except KeyboardInterrupt:
    print("process interrupted by a keyboard input")
    print("process stop")
    client.loop_stop()  # stop the client loop
    client.disconnect()  # disconnect gracefully client.disconnect() client.loop_forever()