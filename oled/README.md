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
![oserror5](https://user-images.githubusercontent.com/28807825/108591916-150ef800-73a6-11eb-9209-a6822702d663.png)  
If the ide report OSError: 5, it is highly possible that your connection with the oled device is not stable.  
It might cause by unreliable cables or in my case bad soldering on the oled pins.   
