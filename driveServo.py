import RPi.GPIO as GPIO
import time
import math

servoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) #GPIO 2 for PWM with 50Hz
p.start(0) #initializing
temp = 0
try:
    while True:
#         p.ChangeDutyCycle(math.sin(temp))
#         temp += math.pi/12
#         
      
        p.ChangeDutyCycle(1)
        time.sleep(0.5)
        p.ChangeDutyCycle(2)
        time.sleep(0.5)
        p.ChangeDutyCycle(3)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(3)
        time.sleep(0.5)
        p.ChangeDutyCycle(2)
        time.sleep(0.5)
        p.ChangeDutyCycle(1)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
