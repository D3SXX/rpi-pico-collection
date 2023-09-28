import machine
import time

led = machine.Pin("LED",machine.Pin.OUT)
def toggle(on, off):
     led.value(1)
     time.sleep(on)
     led.value(0)
     time.sleep(off)

def set_pwm(pin, resolution, value, freq):
    max_value = 2 ** resolution - 1
    if value < 0:
        value = 0
    elif value > max_value:
        value = max_value
    duty_cycle = value / max_value * 100
    time = 1 / freq
    on = (duty_cycle * time) / 100
    off = time - on
    print(f"duty = {duty_cycle}% T = {time}s, on = {on}s, off = {off}s")
    
    toggle(on, off)
   
if __name__ == '__main__':
    i = 255
    while True:
        if i > 0:
            i = i - 1
        else:
            i = 255
        set_pwm(4,8,i, 100)

