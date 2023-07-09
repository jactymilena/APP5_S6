import paho.mqtt.client as mqtt
import json

import consts
from db.database import Database


class Archive:

    def __init__(self):
        self.db = Database('db/archive.csv')
        self.mqtt_setup()

    
    def get_employees(self):
        return self.db.get_all()


    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(consts.topic)


    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode('utf-8'))
        if consts.arrival_time in payload:
            self.db.update(payload['uuid'], consts.arrival_time, payload[consts.arrival_time])
            self.db.update(payload['uuid'], consts.exit_time, '-')
        elif consts.exit_time in payload:
            self.db.update(payload['uuid'], consts.exit_time, payload[consts.exit_time])


    def on_disconnect(self, client, userdata, rc):
        client.loop_stop(force=False)
        if rc != 0:
            print("Unexpected disconnection.")
        else:
            print("Disconnected")


    def mqtt_setup(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_disconnect = self.on_disconnect
        client.connect(consts.mqtt_host, 1883, 60)
        client.loop_start()

