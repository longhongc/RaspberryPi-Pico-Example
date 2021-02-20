from machine import Pin, UART
import utime

uart = UART(0, 115200)  # init with given baudrate

while True:
    uart.write("Hello" + "\n")   
    utime.sleep(1)