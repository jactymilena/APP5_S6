import paho.mqtt.client as mqtt
import json

import consts
from db.database import Database

db = Database('db/users.csv')


def on_connect(client, userdata, flags, rc):
    client.subscribe(consts.topic)


def on_message(client, userdata, msg):
    # client.publish(pub_topic, "MESSAGE")
    print("Update db here")
    payload = json.loads(msg.payload.decode('utf-8'))
    print(payload)



def setup():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(consts.mqtt_host)
    client.loop_start()

