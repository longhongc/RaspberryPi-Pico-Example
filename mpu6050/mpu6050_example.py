from machine import I2C, Pin
import utime
import mpu6050
i2c = I2C(0, scl=Pin(21), sda=Pin(20))
accelerometer = mpu6050.accel(i2c)

while True:
    print(accelerometer.get_values())
    utime.sleep(1)