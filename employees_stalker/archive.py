import paho.mqtt.client as mqtt
import consts


def on_connect(client, userdata, flags, rc):
    client.subscribe(consts.topic)


def on_message(client, userdata, msg):
    # client.publish(pub_topic, "MESSAGE")
    print("Update db here")


def setup():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(consts.mqtt_host)
    client.loop_start()

