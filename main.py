# Imports all of picozero using * and imports sleep
from picozero import *
from time import sleep

"""
The different sections in order are:
- RGB light
- Potentiometer and fan
- Lights with buttons
"""

# Ports for the RGB Light
RGB_red = 5
RGB_green = 8
RGB_blue = 9

# RGB Ports for rgb object
rgb = RGBLED(RGB_red, RGB_green, RGB_blue)

# Color Values for RGB Light
valuesRGB = [0,0,0]

# Buttons for RGB Light
ButtonR = Button(2)
ButtonG = Button(3)
ButtonB = Button(4)

# Ports for controlling Fan backwards and forwards
FanMotor = Motor(0,1,False)

# Port for Potentiometer for fan
# Potential = Potentiometer(16)

# Ports for controlling lights
Light1 = LED(6)
Light2 = LED(10)
Light3 = LED(14)

# Ports for Light Buttons
Button1 = Button(7)
Button2 = Button(11)
Button3 = Button(15)

while True:
    # Set and Reset Red Value
    if ButtonR.is_pressed:
        valuesRGB[0] = 255
    if ButtonR.is_open:
        valuesRGB[0] = 0

    # Set and Reset Green Value
    if ButtonG.is_pressed:
        valuesRGB[1] = 255
    if ButtonG.is_open:
        valuesRGB[1] = 0

    # Set and Reset Blue Value
    if ButtonB.is_pressed:
        valuesRGB[2] = 255
    if ButtonB.is_open:
        valuesRGB[2] = 0

    # Creates Output
    rgb.color = valuesRGB
    sleep(0.1)

