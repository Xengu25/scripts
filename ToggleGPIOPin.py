import RPi.GPIO as GPIO

#Vars
LED = 4
STATE = True

#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

#Set STATE Variable from Pin State
if GPIO.input(LED) == 1:
    STATE = True
else:
    STATE = False

#Reverse GPIO PIN output
if STATE:
    GPIO.output(LED, GPIO.LOW)
    STATE = not STATE
else:
    GPIO.output(LED, GPIO.HIGH)
    STATE = not STATE