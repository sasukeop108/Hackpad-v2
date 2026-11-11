# Hackpad-v2

Hii! This is a hackpad with 16 keys, 15 sk6812-e mini leds, a xiao rp2040 devolopment board and 16 zener diode 1n4148 with a case made using the fusion 360 software with a lid . It uses the 4*4 matrix to use less pins . The pcb was designed using the help of the pcb  software kicad. This is really basic hardware project and i have built this before but im building this once again with more keys to get back on hardware as i havent shipped any hardware project for months. It is made using the hackpad.hackclub.com guide Made for the event embassy.hackclub.com . It uses circuit python and kmk softwares.

## Schematics
<img width="3508" height="2480" alt="image" src="https://github.com/user-attachments/assets/8101705e-31fb-42fe-a4a6-4f9628a4034b" />

## PCB
<img width="230" height="283" alt="image" src="https://github.com/user-attachments/assets/18ba61bb-483d-4b25-b80e-5c1d2c26a240" />

<img width="598" height="655" alt="image" src="https://github.com/user-attachments/assets/e87b99e4-e114-4289-94cb-bd8514f3d72b" />

## Assembly
<img width="615" height="645" alt="image" src="https://github.com/user-attachments/assets/d8956917-02f9-4c63-8eaf-d31c27c192cc" />

 ## Lid
 <img width="590" height="584" alt="image" src="https://github.com/user-attachments/assets/74e5b0f1-d7c0-4b7e-ba4a-25daf8a1e49d" />
 
## Case
<img width="558" height="636" alt="image" src="https://github.com/user-attachments/assets/55e7ba48-1a7d-4c57-a6fd-7bb627043831" />

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

First, solder the smaller components like the diodes and the sk6812 mini-e led. Then solder components like the rp2040 and switches. Download circuit python in your rp2040 and export the firmware.py code in your rp2040 storage. Assemble it in the 3d printed case available in /CAD folder. Woah! Your now good to go with a hackpad.

## Sourcing guide

Download the gerber file in the repo, paste it in any pcb fabrication service page and order your pcb! You could even change anything using the kicad files and this is fully opensource!.

## AI usage disclosure
Used AI to debug the error cause of which i was unable to push readme from vscode to repo and made it fix the issue

## Credits
- embassy.hackclub.com
- Hackpad.hackclub.com
- www.hackclub.com
