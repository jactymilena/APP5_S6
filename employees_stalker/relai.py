import paho.mqtt.client as mqtt
import consts


def on_connect(client, userdata, flags, rc):
    client.publish(consts.topic, "STARTING SERVER")
    client.publish(consts.topic, "CONNECTED")


class Relai:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.connect(consts.mqtt_host)
        self.client.loop_start()

    def publish_user(self, uuid, time):
        self.client.publish(consts.topic, f"{uuid}:{time}")


    

