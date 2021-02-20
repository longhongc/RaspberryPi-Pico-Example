from machine import Pin,I2C
import utime
from ssd1306 import SSD1306_I2C

i2c=I2C(0, sda=Pin(20), scl=Pin(21), freq=40000)


oled = SSD1306_I2C(128, 64, i2c)

oled.text('Welcome to the', 0, 0)
oled.text('Pi Pico', 0, 10)
oled.text('Display Demo', 0, 20)
oled.show()
utime.sleep(4)

oled.fill(1)
oled.show()
utime.sleep(2)
oled.fill(0)
oled.show()

while True:
    oled.text("Hello World", 0, 0)
    for i in range(0, 164):
        oled.scroll(1, 0)
        oled.show()
        utime.sleep(0.01)