
from machine import Pin, Timer
import time
led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(delay):
    global led
    led.value(0)
    time.sleep(delay/1000)
    led.value(1)
    time.sleep(delay/1000)
    

if __name__ == '__main__':
    while True:
        for i in range(0,300):
            tick(i)
            print(i)
        for i in range(300,0):
            tick(i)
            print(i)

