import esp32
import machine
from machine import Pin
from .umqtt.robust import MQTTClient

mqttHost = "192.168.0.1"
mqttTopic = b"wled/82ccd0/api"

alarmMessage = b"{\"on\":true, \"ps\":2}"
okMessage = b"{\"on\":true, \"ps\":1}"

pin = Pin(14, Pin.IN)

if machine.wake_reason() == machine.DEEPSLEEP_RESET:
    print("Waking from deepsleep!")
    c = MQTTClient("garage_door", mqttHost)
    c.connect()
    c.publish(mqttTopic, alarmMessage)    
    
    esp32.wake_on_ext0(pin, esp32.WAKEUP_ALL_LOW)
    machine.lightsleep()

    c.publish(mqttTopic, okMessage)
    c.disconnect()

esp32.wake_on_ext0(pin, esp32.WAKEUP_ANY_HIGH)
machine.deepsleep()
