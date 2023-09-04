import esp32
import machine
import network
import time
from machine import Pin
from .umqtt.robust import MQTTClient

mqttHost = "192.168.0.1"
mqttTopic = b"wled/82ccd0/api"

alarmMessage = b"{\"on\":true, \"ps\":2}"
okMessage = b"{\"on\":true, \"ps\":1}"

pin = Pin(14, Pin.IN)

if machine.wake_reason() == machine.PIN_WAKE:
    print("Waking from deepsleep!")
    c = MQTTClient("garage_door", mqttHost, keepalive=30)
    c.connect()
    c.publish(mqttTopic, alarmMessage)    
    c.disconnect()
    print("MQTT pushed")
    time.sleep(10) 
    print("Entering lightsleep")
    esp32.wake_on_ext0(pin, esp32.WAKEUP_ALL_LOW)
    machine.lightsleep()
    print("Waking from lightsleep")
    
    wlan = network.WLAN(network.STA_IF)
    while not wlan.isconnected():
        print("waiting on wifi")
        time.sleep(1)

    # c = MQTTClient("garage_door", mqttHost, keepalive=30)
    # c.connect()
    c.publish(mqttTopic, okMessage)
    c.disconnect()
    time.sleep(10)

esp32.wake_on_ext0(pin, esp32.WAKEUP_ANY_HIGH)
machine.deepsleep()
