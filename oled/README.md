# OLED Display
the oled module in the example uses the ssd1306 controller

## Install ssd1306 library 
1. Plug in pico
2. Open ide Thonny
3. Select Tools-> Manage pakages
4. Search for ssd1306
5. Install micropython-ssd1306

## Wiring  
**I2C**:  
```
Pico           Oled    
Gnd       ->    Gnd  
3v3       ->    VCC  
SCL(GP21) ->    SCL  
SDA(GP20) ->    SDA  
```

## Demo  
![oled_demo2](https://user-images.githubusercontent.com/28807825/108592751-68834500-73aa-11eb-893c-d8ac761930fe.jpg)

## Error Cases
**OSError 5**:  
![oserror5](https://user-images.githubusercontent.com/28807825/108591916-150ef800-73a6-11eb-9209-a6822702d663.png)  
If the ide report OSError: 5, it is highly possible that your connection with the oled device is not stable.  
It might cause by unreliable cables or in my case bad soldering on the oled pins.   
