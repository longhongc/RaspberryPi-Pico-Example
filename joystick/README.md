# JoyStick

## Wiring
```
Pico             JoyStick    
Gnd          ->    Gnd  
3v3          ->    VCC  
ADC0(GP27)   ->    Y 
ADC1(GP26)   ->    X 
GP22         ->    B
```

## Demo
![joysitck_demo1](https://user-images.githubusercontent.com/28807825/108597351-9032d700-73c3-11eb-97e8-f60ba5c632b2.png)  
![joysitck_demo2](https://user-images.githubusercontent.com/28807825/108597370-ab9de200-73c3-11eb-8456-51e6d33e9025.jpg)  
- Pico has 12 bits adc, but the function read_u16 returns 16 bits Integer from 0 ~ 65535    

![joystick_demo3](https://user-images.githubusercontent.com/28807825/108597432-f4559b00-73c3-11eb-9e6c-f023112258c8.jpg)
