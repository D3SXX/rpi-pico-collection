import machine
import utime

sensor_temp = machine.ADC(26)
conversion_factor = 3.3 / (65535)

A = 3.9083*1E-3;
B = -5.775*1E-7;
C = -4.183*1E-12;
R0 = 100;
RT = 992

while True:
    raw_input = 0
    for i in range(10):
        raw_input += sensor_temp.read_u16()
        utime.sleep(0.05)
    voltage = raw_input / 10 * conversion_factor
    R = RT*(3.3/voltage-1)
    if R > 1000:
        T = (R-R0)/(R0*A)
    else:
        T = "T<0"
    print(f"ADC:{raw_input / 10} V: {voltage} R: {R} Temperature: {T}")
    utime.sleep(1)
