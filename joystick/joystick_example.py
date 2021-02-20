import machine
import utime

x_pin = machine.ADC(26)
y_pin = machine.ADC(27)
b_pin = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    print("X vlaue is {}".format(x_pin.read_u16()))
    print("Y vlaue is {}".format(y_pin.read_u16()))
    if b_pin==1:
        print("attack")
    utime.sleep(0.5)