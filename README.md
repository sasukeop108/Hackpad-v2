# Hackpad-v2

Hii! This is a hackpad with 16 keys, 15 sk6812-e mini leds, a xiao rp2040 devolopment board and 16 zener diode 1n4148 with a case made using the fusion 360 software with a lid . It uses the 4*4 matrix to use less pins . The pcb was designed using the help of the pcb  software kicad. This is really basic hardware project and i have built this before but im building this once again with more keys to get back on hardware as i havent shipped any hardware project for months. It is made using the hackpad.hackclub.com guide Made for the event embassy.hackclub.com . It uses circuit python and kmk softwares.

## BOM
|Quantity|Name         |price            |purpose                       |
|--------|-------------|-----------------|------------------------------|
|1       |Xiao rp2040  |already available|for microcontrolling          |
|16      |cherry mx    |already available|the keys                      |
|16      |sk6812 mini-e|already available|rgb lights which keep changing|
|16      |blank keycaps|already available|to identify key               |
|16      |1n4148 diode |already available|to prevent ghosting of current|
|4       |M3 screws    |already available|to mount case                 |

## Building guide

First, solder the smaller components like the diodes and the sk6812 mini-e led. Then solder components like the rp2040 and switches. Download circuit python in your rp2040 and export the firmware.py code in your rp2040 storage. Woah! Your now good to go with a hackpad.

## Sourcing guide

Download the gerber file in the repo, paste it in any pcb fabrication service page and order your pcb! You could even change anything using the kicad files and this is fully opensource!.

## Credits
- embassy.hackclub.com
- Hackpad.hackclub.com
- www.hackclub.com