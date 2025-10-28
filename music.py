from math import *

"""
In order to take the waveform of an mp3 and convert it into a function capable of playing music
on the pico speakers, it will be necessary to use a Fourier Transform in order to create a
function that can take time t and extract a frequency that roughly mimics the tune of the
original song, or I can manually extract the necessary values beforehand and then input it
manually in code form (inefficient)

Unfortunately it appears that high-quality audio isn't possible without an external audio processor
and so a simple 8-bit song composed of blends and tones will have to do

Song of choice: idk yet lmao

"""
