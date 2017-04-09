import RPi.GPIO as GPIO
led_pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

def fan_open():
    GPIO.output(led_pin, False)

def fan_close():
    GPIO.output(led_pin, True)