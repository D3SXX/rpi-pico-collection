import machine
import utime

sensor_temp = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    raw_input = 0
    for i in range(10):
        raw_input += sensor_temp.read_u16()
        utime.sleep(0.05)
    voltage = raw_input / 10 * conversion_factor
    print(f"ADC:{raw_input / 10} V: {voltage} Temperature: {voltage*100}")
    utime.sleep(1)
