# Bluetooth
The bluetooth module in the example is hc-05 (a yellow check on the module)  
![bt_demo1](https://user-images.githubusercontent.com/28807825/108593592-8acb9180-73af-11eb-9c64-db0283c14ec2.jpg)   
HC-05 default setting:
- default device: HC-05
- default password: 1234
- defaul baudrate: 9600  
Use AT-command to change the setting of hc-05  
https://www.instructables.com/AT-command-mode-of-HC-05-Bluetooth-module/

## Library or Driver
Bluetooth uses UART to transmit data, it doesn't require additional libraries.


## Wiring
UART:
```
Pico           hc-05    
Gnd       ->    Gnd  
3v3       ->    VCC  
TX(GP0)   ->    RX 
RX(GP1)   ->    TX 
                STATE
                EN
```
- Pico uses uart0 as the default uart.  
- The STATE and EN pin is not important in this example.  

## Demo
![bt_demo2](https://user-images.githubusercontent.com/28807825/108593687-29f08900-73b0-11eb-8a2c-730d0ccf72d2.jpg)  
Install a bluetooth receiver app on your phone.  
I recommend this [serial bluetooth terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=zh_TW&gl=US)  
![bt_demo3](https://user-images.githubusercontent.com/28807825/108593634-cc5c3c80-73af-11eb-91bd-7aad028e660c.jpg)

