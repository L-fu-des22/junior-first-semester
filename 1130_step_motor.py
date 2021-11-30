
import RPi.GPIO as GPIO
import time

PUL1 = 11
DIR1 = 12
PUL2 = 13
DIR2 = 15
pinlist = [PUL1, DIR1, PUL2, DIR2]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pinlist, GPIO.OUT)
GPIO.output(pinlist,0)

# Stepper PWM
stepper = GPIO.PWM(PUL1,350)

def run(direction,t):
    GPIO.output(DIR1,direction)
    stepper.start(30)
    time.sleep(int(t))

def stop():
    stepper.stop()
   
def Stepper_motion(time):
    direction = 1
    while True:
        run(direction, time)
        stop()

Stepper_motion(100)
    
#     while True:
#         if limit() == True:
#             run(direction,1)
#             con = 0
#             continue
#         elif limit() == False and con == 0:
#             if direction == 1:
#                 direction = 0
#                 con = 1
#             elif direction == 0:
#                 direction = 1
#                 con = 1
#             stop()
#             continue 
   

