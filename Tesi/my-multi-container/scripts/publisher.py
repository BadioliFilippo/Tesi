import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883
topic = "test/topic"

def on_publish(client, userdata, mid, properties=None, reason_code=None):
    print("Messaggio pubblicato con MID:", mid)

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv5, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

    client.on_publish = on_publish
    client.connect(broker, port)
    client.loop_start()
    message = "Ciao"
    result = client.publish(topic, message)

    status = result[0]
    print(status)
    
    if status == 0:
        print(f"Inviato messaggio '{message}' al topic '{topic}' ")
    else:
        print(f"Errore nell'invio messaggio al topic {topic}")

    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()