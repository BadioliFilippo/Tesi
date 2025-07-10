import paho.mqtt.client as mqtt
import time

broker = "test.mosquitto.org"
port = 8080
mongo_uri = "mongodb://mongo:27017"
topic = "test/topic"

def on_connect(client, userdata, flags, reason_code):
    print("Connected with reason code:", reason_code)
    client.subscribe(topic)

def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()} on topic {message.topic}")

def main():
    client = mqtt.Client(transport="websockets")
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