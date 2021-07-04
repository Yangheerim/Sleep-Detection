import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT) #led

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("connect OK")
	else:
		print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
	print(str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
	rcvmsg = str(msg.payload.decode("utf-8"))
	print(rcvmsg)
	if rcvmsg == "Sleeping":
		print("Sleeping~~")
		GPIO.output(27, GPIO.HIGH)
	else:
		print("Not Sleeping~~")
		GPIO.output(27, GPIO.LOW)

# create MQTT client
client = mqtt.Client()

# register callback function
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

# address : brocker(server) IP, port: 1883(default port number)
client.connect("172.20.10.6", 1883)
# subscibe topic with data
client.subscribe("hello/world")
client.loop_forever()
