# Imports all of picozero using * and imports sleep
from picozero import *
from time import sleep

"""
The different sections in order are:
- RGB light
- Potentiometer and fan
- Lights with buttons
- Speaker hooked up to button
"""

# Ports for the RGB Light
RGB_red = 21
RGB_blue = 20
RGB_green = 19

# Ports for controlling Fan backwards and forwards
FanMotor = Motor(0,1,False)

# Port for Potentiometer for fan
Potential = Potentiometer(16)

# Ports for controlling lights
Light1 = LED(6)
Light2 = LED(10)
Light3 = LED(14)

# Ports for Light Buttons
Button1 = Button(7)
Button2 = Button(11)
Button3 = Button(15)

# Speaker is configured in a separate file due to complexity
# Speaker Button and pin
SpeakButton = Button(29)

while True:
    