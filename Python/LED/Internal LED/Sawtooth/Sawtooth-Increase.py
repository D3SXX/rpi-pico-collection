# Sawtooth internal LED example
# Using Pulse Width Modulation logic

from machine import Pin, Timer
import time

led = Pin("LED", Pin.OUT)
tim = Timer()

def breath(timer):
    freq = 80  # Frequency in Hz
    for duty_cycle in range(-100,0,1):
        # Calculate the on and off times based on the duty cycle
        on_time = 1 / freq * (abs(duty_cycle)/100)
        off_time = 1 / freq * (1 - (abs(duty_cycle)/100))
        led.value(0)
        time.sleep(on_time)
        led.value(1)
        time.sleep(off_time)
        
tim.init(freq=1, mode=Timer.PERIODIC, callback=breath)






