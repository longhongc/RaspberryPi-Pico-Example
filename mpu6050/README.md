# MPU6050 Accelerometer

## library
The mpu6050.py class is modified from https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython 
iic.start() and iic.stop() is removed  

## Wiring
**I2C**:  
```
Pico           MPU6050    
Gnd       ->    Gnd  
3v3       ->    VCC  
SCL(GP21) ->    SCL  
SDA(GP20) ->    SDA  
                XDA
                XCL
                ADD
                INT
```
- The XDA, XCL, ADD, INT pin is not important in this example.

## Demo
![acc_demo1](https://user-images.githubusercontent.com/28807825/108596551-c15dd800-73c0-11eb-9df0-ee397ff55341.jpg)
![acc_demo2](https://user-images.githubusercontent.com/28807825/108596501-6d52f380-73c0-11eb-9e95-577cb690d548.jpg)
