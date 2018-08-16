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
GPIO.setwarnings(False)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.output(LEDPIN,GPIO.LOW)

# url to IOTA full node when checking balance on IOTA tangle
iotaNode = "....."      # check if full node is added

# creating a IOTA object
api = Iota(iotaNode, "")

# IOTA address to be checked for funds
address =[Address(b'9JVCOSTCHHMYD9QBPPJBCNSZDQQRBRELXBXS9CDGINCQPCNFKLHLEQCGGRAOYMCWRZDNXXFALMV9I99LXQZSBDFZJW')]

# function for checking balance on a iota adress
def checkAddressBalance():
    print ("checking address balance.....")
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    return (balance[0])

print checkAddressBalance()

time.sleep(10)



