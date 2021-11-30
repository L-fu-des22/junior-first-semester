import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

in1 = 38
in2 = 40

GPIO.setmode(GPIO.BOARD)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

while(1):
    print( "First calibrate by giving some +ve and -ve values.....")

    x1=int(input())
    
    if x1==0:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        time.sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
    if x1==1:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.cleanup()
pwm1.stop()
pwm2.stop()