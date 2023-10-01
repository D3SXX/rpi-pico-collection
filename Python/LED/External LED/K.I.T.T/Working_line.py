from machine import Pin, Timer
import time

# Define the LED pins
led_pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)]

delay = 0.1
freq = 80
tim = Timer()

def fade_in(led):
    for duty_cycle in range(0, 101, 1):
        on_time = 1 / freq * (duty_cycle / 100)
        off_time = 1 / freq * (1 - (duty_cycle / 100))
        led.value(1)
        time.sleep(on_time)
        led.value(0)
        time.sleep(off_time)

def fade_out(led):
    for duty_cycle in range(100, -1, -1):
        on_time = 1 / freq * (duty_cycle / 100)
        off_time = 1 / freq * (1 - (duty_cycle / 100))
        led.value(1)
        time.sleep(on_time)
        led.value(0)
        time.sleep(off_time)

# Initialize the timers for LED movement
for i in range(5):
    for led in led_pins:
        led.value(0)  # Turn off all LEDs
    led_pins[i].value(1)  # Turn on the current LED
    time.sleep(0.5)  # Delay to show the current LED
    fade_out(led_pins[i])  # Fade out the current LED
    time.sleep(0.5)  # Delay before moving to the next LED

# Move LED from right to left
for i in range(3):
    for led in led_pins:
        fade_in(led)  # Fade in all LEDs
        time.sleep(0.1)  # Delay to show all LEDs
        fade_out(led)  # Fade out all LEDs
        time.sleep(0.1)  # Delay before next iteration

# Move LED from left to right
for i in range(3):
    for led in reversed(led_pins):
        fade_in(led)  # Fade in all LEDs
        time.sleep(0.1)  # Delay to show all LEDs
        fade_out(led)  # Fade out all LEDs
        time.sleep(0.1)  # Delay before next iteration

