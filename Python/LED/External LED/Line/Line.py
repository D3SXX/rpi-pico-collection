# Making a Line effect with 5 external LEDs example

from machine import Pin, Timer
import time

led_1 = Pin(0, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(2, Pin.OUT)
led_4 = Pin(3, Pin.OUT)
led_5 = Pin(4, Pin.OUT)

delay = 0.1
while True:
     led_1.value(1)
     time.sleep(delay)
     led_2.value(1)
     time.sleep(delay)
     led_3.value(1)
     time.sleep(delay)
     led_4.value(1)
     time.sleep(delay)
     led_5.value(1)
     time.sleep(delay)
     led_1.value(0)
     time.sleep(delay)
     led_2.value(0)
     time.sleep(delay)
     led_3.value(0)
     time.sleep(delay)
     led_4.value(0)
     time.sleep(delay)
     led_5.value(0)
     time.sleep(delay)
     

