import machine
import utime
import time

def breath(delay_sec):
    freq = 500 / delay_sec  # Frequency in Hz
    for duty_cycle in range(-100,100,1):
        # Calculate the on and off times based on the duty cycle
        on_time = 1 / freq * (abs(duty_cycle)/100)
        off_time = 1 / freq * (1 - (abs(duty_cycle)/100))
        led.value(0)
        time.sleep(on_time)
        led.value(1)
        time.sleep(off_time)
    # Turn off led
    led.value(0)

if __name__ == '__main__':
    delay_sec = 1
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    led = machine.Pin("LED", machine.Pin.OUT)
    tim = machine.Timer()
    while True:
        ADC = sensor_temp.read_u16()
        reading = ADC * conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        print(f"ADC: {ADC} Voltage: {reading} temperature: {temperature:.2f}")
        breath(delay_sec)
        utime.sleep(delay_sec)

