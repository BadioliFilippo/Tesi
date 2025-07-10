import paho.mqtt.client as mqtt
import time
from pymongo import MongoClient

broker = "mosquitto"
port = 1883
mongo_uri = "mongodb://mongo:27017"
sensors = ["Watch", "Expressions", "Distractions"]
topics = [f"Sensor/{name}" for name in sensors]

clientM = MongoClient(mongo_uri)
db = clientM["SensorData"]
collection = db["Sensor"]
def on_connect(client, userdata, flags, reason_code):
    print("Connected with reason code:", reason_code)
    for topic in topics:
        client.subscribe(topic)

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()} on topic {message.topic}")
    collection.insert_one({f"{message.topic}" : message.payload.decode()})

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(broker, port, keepalive=60)
    except Exception as e:
        print("Errore di connessione", e)
    

    client.loop_start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programma terminato dall'utente")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()