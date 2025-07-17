import paho.mqtt.client as mqtt
import random

broker = "mosquitto"
port = 1883
sensors = ["Watch", "Distractions", "Expressions"]
topics = [f"Sensor/{name}" for name in sensors]
rand = random.choice(sensors)

def on_publish(client, userdata, mid, properties=None):
    print("Messaggio pubblicato con MID:", mid)

def watch():
    return f"BPM = {random.randint(80, 120)}"

def distr():
    return f"Distracted by {random.choice(['Smartphone', 'Outside event', 'Radio dashboard'])}"

def expr():
    return f"Driver face: {random.choice(['Sneezing', 'Yawning', 'Sleepy', 'Angry'])}"

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_publish = on_publish
    client.connect(broker, port)
    client.loop_start()

    match rand:
        case "Watch": 
            message = watch()
            topic = topics[0]
        case "Distractions": 
            message = distr()
            topic = topics[1]
        case "Expressions": 
            message = expr()
            topic = topics[2]

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