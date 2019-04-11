# External module imports
import RPi.GPIO as GPIO
import time
import json
import operator
import requests

# Pin
rightMotor   = 16 # Broadcom pin 4 (P1 pin 16)
leftMotor  = 18 # Broadcom pin 5 (P1 pin 18)
dirPin0 = 13
dirPin1 = 15

#api-endpoint
URL = "http://helpmegethome.live/move"

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(leftMotor, GPIO.OUT, initial=GPIO.LOW) # LED pin set as output
GPIO.setup(rightMotor, GPIO.OUT, initial=GPIO.LOW) # PWM pin set as output

def stopMotion():
    GPIO.output(leftMotor, GPIO.LOW)
    GPIO.output(rightMotor, GPIO.LOW)
    return
    
print("Setup complete")
try:
    while True:
        
        #getting jason payload
        r = requests.get(url = URL)
        data = r.json()
        dir = max(data, key=data.get)
        
        if dir == "backward":
            print("move backward")
            stopMotion()
            time.sleep(2)
            stopMotion()
        elif dir == "forward":
            print("move forward")
            GPIO.output(leftMotor, GPIO.HIGH)
            GPIO.output(rightMotor, GPIO.HIGH)
            time.sleep(2)
            stopMotion()
        elif dir == "left":
            print("move left")
            GPIO.output(leftMotor, GPIO.LOW)
            GPIO.output(rightMotor, GPIO.HIGH)
            time.sleep(0.3)
            stopMotion()
        elif dir == "right":
            print("move right")
            GPIO.output(leftMotor, GPIO.HIGH)
            GPIO.output(rightMotor, GPIO.LOW)
            time.sleep(0.3)
            stopMotion()
        else:
            stopMotion()
        time.sleep(2.5)


  
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
