# LoStik code examples
This repository contains code examples in Python to use with the LoStik device.

LoStick is a open source USB LoRa® device available here https://www.crowdsupply.com/ronoth/lostik. Its main characteristics are:
* Works with any PC, Raspberry Pi, or BeagleBone
* Simple ASCII interface
* Supports Packet mode LoRa® (packet mode) or LoRaWAN™
* Compatible with The Things Network and Loriot
* Based on the RN2903/R2483 by Microchip

**Main references used**
* The example here are basically based on those in: https://github.com/lolsborn/LoStik
* Some help also from here: https://github.com/raspberrypi-tw/lora

## Code examples

Before executing the code below: 
* check whether the channel parameters are properly set.
* discover the serial port where the Lostik is connected (```_lostik-serial-port_```). For example in _macOS_ with command:```ls /dev/cu.*``` 

### Support files:
* ```miniterm.py```: used to connect to a LoStick and send commands manually
* ```packer.py```: support file

### file: ```sender.py```
- sends using Lora a text message red from input
- execute as: ```python sender.py _lostik-serial-port_```

### file: ```senderp.py```
- periodically sends using Lora a text message stored in variable "rawinput"
- execute as: ```python senderp.py _lostik-serial-port_```

### file: ```receiver.py```
- continuously reads messages using Lora
- execute as: ```python receiver.py _lostik-serial-port_```

### file: ```senderp_loriot.py```
- periodically sends using LoRaWAN  a text message stored in variable "rawinput"
- uses OTAA and https://www.loriot.io/ servers
- execute as: ```python senderp_loriot.py _lostik-serial-port_```
