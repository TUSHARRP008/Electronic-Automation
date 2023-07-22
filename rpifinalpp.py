from firebase import firebase
import RPi.GPIO as GPIO
import time 
firebase=firebase.FirebaseApplication('https://electronic-automation-ad328.firebaseio.com',None) 
GPIO.setmode(GPIO.BCM) 
while True:
    result1=firebase.get('/LED_STATUS',None)
    result2=firebase.get('/FAN_STATUS',None)
    print (result1)
    if(result1==1):
        GPIO.setwarnings(False)
        GPIO.setup(11,GPIO.OUT)
        GPIO.output(11,False)
    if(result1==0):
        GPIO.setwarnings(False)
        GPIO.setup(11,GPIO.OUT)
        GPIO.output(11,True)
    if(result2==1):
        GPIO.setwarnings(False)
        GPIO.setup(9,GPIO.OUT)
        GPIO.output(9,False)
    if(result2==0):
        GPIO.setwarnings(False)
        GPIO.setup(9,GPIO.OUT)
        GPIO.output(9,True)

