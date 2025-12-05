
# Imports all of picozero using * and imports sleep
from picozero import *
from time import sleep

"""
The different sections in order are:
- RGB light
- Potentiometer and fan
- Lights with buttons

There will be no music just a buzzer
"""

# Toggle for RGB and 3 lights
toggleRGB = 0

# Ports for the RGB Light
RGB_red = 5
RGB_green = 8
RGB_blue = 9

# RGB Ports for rgb object
rgb = RGBLED(RGB_red, RGB_green, RGB_blue)

# Color Values for RGB Light
valuesRGB = [0,0,0]

'''
No longer relevant as I don't have enough ports to bother with this
# Buttons for RGB Light
ButtonR = Button(2)
ButtonG = Button(3)
ButtonB = Button(4)
'''

# Ports for controlling Fan backwards and forwards
FanMotor = Motor(0,1,False)


# Port for Potentiometer for fan
Potential = Potentiometer(16)


# Ports for controlling lights
Light1 = LED(17)
Light2 = LED(20)
Light3 = LED(19)

# Ports for Light Buttons
# Red
Button1 = Button(13)
# Green
Button2 = Button(14)
# Blue/Yellow
Button3 = Button(15)

# Function for the first update loop for the first core
def updateloop1():
    if toggleRGB == 0:
        # Set and Reset Red Value
        if Button1.is_pressed:
            valuesRGB[0] = 255
        else:
            valuesRGB[0] = 0

        # Set and Reset Green Value
        if Button2.is_pressed:
            valuesRGB[1] = 255
        else:
            valuesRGB[1] = 0

        # Set and Reset Blue Value
        if Button2.is_pressed:
            valuesRGB[2] = 255
        else:
            valuesRGB[2] = 0
    else:
        # Set and Reset Values for non-RGB lights
        if Button1.is_pressed:
            Light1.on()
            print("button1")
        else:
            Light1.off()

        if Button2.is_pressed:
            Light2.on()
            print("button2")
        else:
            Light2.off()
        
        if Button3.is_pressed:
            Light3.on()
            print("button3")
        else:
            Light3.off()
      
    # Potentiometer and Motor Setup
    if Potential.value == true:
        FanMotor.forward()
    else:
        FanMotor.off
    
    # Creates Output for RGBLED
    rgb.color = valuesRGB

while True:
    updateloop1()
    sleep(0.1)
    print("resetloop")



