from machine import Pin, ADC
import utime

x_pin = ADC(26)
y_pin = ADC(27)
b_pin = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    print("X vlaue is {}".format(x_pin.read_u16()))
    print("Y vlaue is {}".format(y_pin.read_u16()))
    if b_pin==1:
        print("button pressed")
    utime.sleep(0.5)