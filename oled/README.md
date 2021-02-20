# OLED Display
the oled module in the example uses the ssd1306 controller

## Install ssd1306 library 
1. Plug in pico
2. Open ide Thonny
3. Select Tools-> Manage pakages
4. Search for ssd1306
5. Install micropython-ssd1306

## Error Cases
**OSError 5**:  
![](https://github.com/longhongc/RaspberryPi-Pico-Example/issues/1#issue-812570252)
If the ide report OSError: 5, it is highly possible that your connection with the oled device is not stable.  
It might cause by unreliable cables or in my case bad soldering on the oled pins.   
