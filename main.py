# Import functions from music and ComponentFunctions in for the threaded update loops
from ComponentFunctions import *
from music import *

# Prepare for the threading process in order to have music and functions in tandem
from _thread import *
import machine

from time import sleep

while True:
    updateLoop1()
