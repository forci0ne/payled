# LEDPAY version 0.1 based on a tutorial by Hugo Gregersen (Integrating physical devices with IOTA)

# import some python date and time functions
import time
import datetime

# imports the GPIO library
import RPi.GPIO as GPIO

# imports the PYOTA library
from iota import Iota
from iota import Address

# setting up the 0/I raspberry pin's
LEDPIN = 18
GPIO.setmode(GPIO.BCM)




