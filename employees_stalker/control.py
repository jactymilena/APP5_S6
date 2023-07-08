import consts
import requests
import time
from machine import Pin


led_pin = Pin(18, Pin.OUT)  

# def allumer_led():
#     led_pin.on()

# def eteindre_led():
#     led_pin.off()


# UID attendu
# TODO: faire un tableau des deux uid qu'on peut avoir 
expected_uid = "91e53efa-0098-4f11-b8a2-e738f2df82e4"

