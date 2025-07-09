import paho.mqtt.client as mqtt

broker = "mosquitto"
port = 1883
mongo_uri = "mongodb://mongo:27017"
topic = "test/topic"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with reason code:", reason_code)

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()} on topic {message.topic}")

def main():
    print("Ciao sono il sub")
    client = mqtt.Client(protocol=mqtt.MQTTv5, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port)
    client.loop_forever()  # loop blocccante che gestisce la connessione e messaggi

if __name__ == "__main__":
    main()