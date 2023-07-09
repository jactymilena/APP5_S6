import paho.mqtt.client as mqtt
import json
import consts
from datetime import datetime
                

class Relai:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect(consts.mqtt_host)
        self.client.loop_start()


    def publish_arrival(self, uuid):
        self.publish_user(uuid, consts.arrival_time)


    def publish_exit(self, uuid):
        self.publish_user(uuid, consts.exit_time)


    def publish_user(self, uuid, event):
        json_msg = json.dumps({
            "uuid": str(uuid),
            event : str(datetime.now())
        })
        
        self.client.publish(consts.topic, json_msg.encode('utf-8'))
