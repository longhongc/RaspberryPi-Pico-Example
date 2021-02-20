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
