#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time 

LED1 = "P9_15"
LED2 = "P9_17"
LED3 = "P9_21"
LED4 = "P9_23"

Button1 = "P9_18"
Button2 = "P9_20"
Button3 = "P9_22"
Button4 = "P9_24"


GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

map = {Button1: LED1, Button2: LED2, Button3: LED3, Button4: LED4}


def updateFunktion(channel):
    state = GPIO.input(channel)

    GPIO.output(map[channel], state)
    print(map[channel] + "Toggled")


GPIO.add_event_detect(Button1, GPIO.BOTH, callback=updateFunktion)
GPIO.add_event_detect(Button2, GPIO.BOTH, callback=updateFunktion)
GPIO.add_event_detect(Button3, GPIO.BOTH, callback=updateFunktion)
GPIO.add_event_detect(Button4, GPIO.BOTH, callback=updateFunktion)


try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()

