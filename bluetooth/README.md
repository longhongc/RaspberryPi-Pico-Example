# Bluetooth
The bluetooth module in the example is hc-05 (a yellow check on the module)  
![bt_demo1](https://user-images.githubusercontent.com/28807825/108593592-8acb9180-73af-11eb-9c64-db0283c14ec2.jpg)

## Library or Driver
Bluetooth uses UART to transmit data, it doesn't require additional library.


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
- Uart requires spcifying the baudrate to establish connection. The default baudrate of hc-05 is 9600. If you want to change the baudrate, you will have to use the AT-command.

## Demo
![bt_demo2](https://user-images.githubusercontent.com/28807825/108593687-29f08900-73b0-11eb-8a2c-730d0ccf72d2.jpg)  
Install a bluetooth receiver app on your phone.  
I recommend this [serial bluetooth terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=zh_TW&gl=US)  
![bt_demo3](https://user-images.githubusercontent.com/28807825/108593634-cc5c3c80-73af-11eb-91bd-7aad028e660c.jpg)

