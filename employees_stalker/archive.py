import paho.mqtt.client as mqtt
import json

import consts
from db.database import Database


db = Database('db/archive.csv')


def on_connect(client, userdata, flags, rc):
    client.subscribe(consts.topic)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    event = consts.arrival_time if consts.arrival_time in payload else exit_time
    db.update(payload['uuid'], event, payload[event])


def on_disconnect(client, userdata, rc):
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")


def setup():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.connect(consts.mqtt_host, 1883, 60)
    client.loop_start()

