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
iotaNode = "https://nodes.iota.fm:443"      # check if full node is added

# creating a IOTA object
api = Iota(iotaNode, "")

# IOTA address to be checked for funds
address =[Address(b'9JVCOSTCHHMYD9QBPPJBCNSZDQQRBRELXBXS9CDGINCQPCNFKLHLEQCGGRAOYMCWRZDNXXFALMV9I99LXQZSBDFZJW')]

# function for checking balance on a iota adress
def checkBalance():
    print ("checking address balance.....")
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    return (balance[0])

# get current balance and use as baseline
currentBalance = checkBalance()
lastbalance = currentbalance

# some variables
lightbalance = 0
balcheckcount = 0
lightstatus = False

# main loop that executes every 1 second
while True:

    #check for new funds and add to lightbalance when found
    if balcheckcount == 10:
        currentbalance = checkBalance()
        if currentbalance > lastbalance:
            lightbalance = lightbalance + (currentbalance - lastbalance)
            lastbalance = currentbalance
        balcheckcount = 0

    # manage light balance and light ON/OFF
    if lightbalance > 0:
        if lightstatus == False:
            print ("light ON")
            GPIO.output(LEDPIN,GPIO.HIGH)
            lightstatus = True
        lightbalance = lightbalance -1

    else:
        if lightstatus == True:
            print("light OFF")
            GPIO.output(LEDPIN,GPIO.LOW)
            lightstatus = False

    # print remaining light balance
    print(datetime.timedelta(seconds=lightbalance))

    # increase balance check counter
    balcheckcount = balcheckcount +1

    # pause for 1 sec
    time.sleep(1)
