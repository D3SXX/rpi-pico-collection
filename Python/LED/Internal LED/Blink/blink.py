# Blinking internal LED example
# Taken from https://github.com/raspberrypi/pico-micropython-examples/blob/master/blink/blink.py

from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
