from machine import Pin, UART, I2C
import utime
import mpu6050
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
accelerometer = mpu6050.accel(i2c)
uart = UART(0, 115200)                         # init with given baudrate

while True:
    uart.write(str(accelerometer.get_values()) + "\n")   # write the 3 characters
    utime.sleep(1)