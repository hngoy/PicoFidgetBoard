
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

# Speaker
speaker = Speaker(27)

# Toggle Button for RGB
toggleButton = Button(28)

# Ports for the RGB Light
RGB_red = 2
RGB_green = 3
RGB_blue = 4

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

    
# Toggle for RGB and 3 lights
toggleRGB = 0

""" Potentiometer dropped
# Port for Potentiometer for fan
Potential = Pot(27)
"""

# Define custom pulse widths (in seconds)
MIN_PULSE = 550 / 1000000 # 550 microseconds
MAX_PULSE = 2400 / 1000000 # 2400 microseconds
servo = Servo(pin=12, min_pulse_width=MIN_PULSE,max_pulse_width=MAX_PULSE)
# Create an object connected to GPIO 0 with custom pulse width

# Ports for controlling lights
Light1 = LED(17)
Light2 = LED(16)
Light3 = LED(22)

def badoom():
    c_note = 523
    speaker.play(c_note, 0.1)
    sleep(0.1)
    speaker.play(c_note, 0.9)

# Ports for Light Buttons
# Red
Button1 = Button(13)
# Green
Button2 = Button(14)
# Blue/Yellow
Button3 = Button(15)

# Function for the first update loop for the first core
def updateloop1(toggleRGB):
    
    # Changes toggle button
    if toggleButton.is_pressed:
        print("toggle changed")
        if toggleRGB == 1:
            toggleRGB = 0
        else:
            toggleRGB = 1
    
    # Turns on LEDs depending on which mode its on
    if toggleRGB == 0:
        # Set and Reset Red Value
        if Button1.is_pressed:
            valuesRGB[0] = 255
            print("R")
        else:
            valuesRGB[0] = 0

        # Set and Reset Green Value
        if Button2.is_pressed:
            valuesRGB[1] = 255
            print("G")
        else:
            valuesRGB[1] = 0

        # Set and Reset Blue Value
        if Button3.is_pressed:
            valuesRGB[2] = 255
            print("B")
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
    
    if Button1.is_pressed or Button2.is_pressed or Button3.is_pressed:
        if Button1.is_pressed and Button2.is_pressed and Button3.is_pressed:
            servo.max()
            badoom()
        else:
            servo.mid()
    else:
        servo.min()
    
    
    # Creates Output for RGBLED
    rgb.color = valuesRGB
    
    return toggleRGB

try:
    while True:
        toggleRGB = updateloop1(toggleRGB)
        sleep(0.1)
        print("resetloop")
    
finally:
    speaker.off()



