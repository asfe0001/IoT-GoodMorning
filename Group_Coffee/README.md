# IoT-GoodMorning: Subproject Coffee

## Goals of the Subproject
- Read the intensity provided by the manager via the MQTT broker
- Control a LEDs and buzzer via inputs from Broker

## List of Requirements Group03
 * Subscribe to topic provided by manager
 * control LED bar and buzzer based on the value given in the topic

 
## Overview Hardware System
* Raspberry PI 3
* LED bar
* Piezo-buzzer

## Preparation for Startup
* install **paho client** with ``sudo pip install paho-mqtt``

## Get / control values
* To get intensity values, subscribe to brokertopic Goodmorning/Kaffee/Kaffeestaerke
* distinguish between three intensity states based on intensity (1-10) given by manager

* 


##  Developers and authors Subproject
 * Dennis Schell
 * Xiaotian Sun
 * Xueying Wang 
 * Jonathan Haller
