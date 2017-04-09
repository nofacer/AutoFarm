import RPi.GPIO as GPIO
import time
import gv

led_pin = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
while True:

    GPIO.output(GPIO_PIN,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GPIO_PIN,GPIO.LOW)
    time.sleep(1)

def cal_fan_spd(temper):
    x=temper-warning
    if x<=0:return 0
else:
    return(int(x))