# Imports all of picozero using * and imports sleep
from picozero import *
from time import sleep

"""
The different sections in order are:
- RGB light
- Potentiometer and fan
- Lights with buttons

Functions and operations for the music section will be held in
the music file instead in order to prevent unnecessary pain and
suffering
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
Potential = Potentiometer(16)

# Ports for controlling lights
Light1 = LED(6)
Light2 = LED(10)
Light3 = LED(14)

# Ports for Light Buttons
Button1 = Button(7)
Button2 = Button(11)
Button3 = Button(15)

# Function for the first update loop for the first core
def updateloop1():
    # Set and Reset Red Value
    if ButtonR.is_pressed:
        valuesRGB[0] = 255
    else:
        valuesRGB[0] = 0

    # Set and Reset Green Value
    if ButtonG.is_pressed:
        valuesRGB[1] = 255
    else:
        valuesRGB[1] = 0

    # Set and Reset Blue Value
    if ButtonB.is_pressed:
        valuesRGB[2] = 255
    else:
        valuesRGB[2] = 0

    # Set and Reset Values for non-RGB lights
    if Button1.is_pressed:
        Light1.on()
    else:
        Light1.off()

    if Button2.is_pressed:
        Light2.on()
    else:
        Light2.off()
        
    if Button3.is_pressed:
        Light3.on()
    else:
        Light3.off()
        
    # Potentiometer and Motor Setup
    if Potential.is_active:
        FanMotor.forward()
    else:
        FanMotor.off

    # Creates Output for RGBLED
    rgb.color = valuesRGB


