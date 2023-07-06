import paho.mqtt.client as mqtt

mqtt_host = '127.0.0.1'
pub_topic = 'hello/test1234'

def on_connect(client, userdata, flags, rc):
    # client.subscribe(sub_topic)
    client.publish(pub_topic, "STARTING SERVER")
    client.publish(pub_topic, "CONNECTED")


# def on_message(client, userdata, msg):
#     client.publish(pub_topic, "MESSAGE")

class Relai:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        # self.client.on_message = on_message
        self.client.connect(mqtt_host)
        self.client.loop_start()

    def publish_uuid(self, uuid, time):
        self.client.publish(pub_topic, f"{uuid}:{time}")


    

