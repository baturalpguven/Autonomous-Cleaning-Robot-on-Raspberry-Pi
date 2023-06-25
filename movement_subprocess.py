import RPi.GPIO as GPIO          
from time import sleep
import time
import sys
import signal
import logging
# import os

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def sonar_sensor(trig,echo):
    GPIO.output(trig, False)
    time.sleep(0.1)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo) == 0 :
        pulse_start = time.time()
    while GPIO.input(echo) == 1 :
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    # if pulse_duration >=0.01746:
    #     print('time out')
    # elif distance > 300 or distance==0:
    #     print('out of range')
    distance = round(distance, 3)
    print ('Distance : %f cm'%distance)
    logging.debug('Distance : %f cm'%distance)
    return distance

GPIO.setmode(GPIO.BCM)
trig = 27 # 7th
echo = 17 # 6th

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

time.sleep(0.5)


in1 = 22 #PIN31
in3 = 24 #PIN35
in2 = 16 #PIN10
in4 = 10 #PIN24
en = 23   #PIN18
en2 = 2  #PIN3
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(en,1000)
p1=GPIO.PWM(en2,1000)
p.start(100)
p1.start(100)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

# os.mkdir("log.txt")
logging.basicConfig(filename="./log.txt",level=logging.DEBUG)

x=input("raw_input: ")
print ('-----------------------------------------------------------------sonar start')
try :
    while True:
        
        
        distance = sonar_sensor(trig,echo)
        
        if distance<5:
            x='s'



        if x=='s':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x=input("raw_input: ")
            # distance = sonar_sensor(trig,echo)

        elif x=='f':
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(en,GPIO.HIGH)
            GPIO.output(en2,GPIO.HIGH)
            temp1=1
            x='z'
            # print(distance)


        elif x=='b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in4,GPIO.HIGH)
            temp1=0
            x='z'
            

        elif x=='1':
            print("left")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif x=='2':
            print("right")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            p1.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            p1.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            p.ChangeDutyCycle(125)
            p1.ChangeDutyCycle(125)
            x='z'
        
        
        elif x=='e':
            GPIO.cleanup()
            break

except:
    GPIO.cleanup()