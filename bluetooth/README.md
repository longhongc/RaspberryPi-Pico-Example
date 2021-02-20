# Bluetooth
The bluetooth module in the example is hc-05 (a yellow check on the module)

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

Install a bluetooth receiver app on your phone.  
I recommend this [serial bluetooth terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=zh_TW&gl=US)



