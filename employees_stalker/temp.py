# from flask import Flask
# import paho.mqtt.client as mqtt

# app = Flask(__name__)
# sub_topic = 'tttt'
# pub_topic = 'hello/test1234'


# def on_connect(client, userdata, flags, rc):
#     client.subscribe(sub_topic)
#     # client.publish(pub_topic, "STARTING SERVER")
#     # client.publish(pub_topic, "CONNECTED")


# def on_message(client, userdata, msg):
#     # client.publish(pub_topic, "MESSAGE")
#     print('on_message')

#     # add last arriv/ to db



# @app.route('/')
# def hello():
#     return 'Hello, World!'


# @app.route('/test')
# def test():
#     return 'This is a test'


# if __name__ == "__main__":
#     client = mqtt.Client()

#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect('127.0.0.1')
#     client.loop_start()

#     app.run(debug=True)
