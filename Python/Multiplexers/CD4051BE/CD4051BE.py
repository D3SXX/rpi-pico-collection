import machine
import time

pin_INH = machine.Pin(12, machine.Pin.OUT) # INH pin in manual (6)
pin_A = machine.Pin(13, machine.Pin.OUT) # A pin in manual (11)
pin_B = machine.Pin(14, machine.Pin.OUT) # B pin in manual (10)
pin_C = machine.Pin(15, machine.Pin.OUT) # C pin in manual (9)
pin_adc = machine.ADC(machine.Pin(26)) # COM OUT/IN (3) in manual

def scan_dc405(delay_sec):
    pin_INH.off()
    for i in range(0,8):
        if i > 7 // 2:
            pin_C.on()
            print("C:1",end=" ")
        else:
            pin_C.off()
            print("C:0",end=" ")
        if i == 0 or i == 1 or i == 4 or i == 5:
            pin_B.off()
            print("B:0",end=" ")
        else:
            pin_B.on()
            print("B:1",end=" ")
        if i % 2 == 0 and not 0:
            pin_A.off()
            print("A:0",end=" ")
        else:
            pin_A.on()
            print("A:1",end=" ")
        adc = pin_adc.read_u16()
        voltage = adc * (3.3) / 65535    
        print(f"CH{i} adc: {adc} voltage: {voltage}")
        time.sleep(delay_sec)
        pin_C.off()
        pin_B.off()
        pin_A.off()

while True:
    delay_sec = 1 # Set up delay time for each scan
    scan_dc405(delay_sec)


