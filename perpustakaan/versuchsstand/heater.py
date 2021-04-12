import RPi.GPIO as GPIO


def init_heater():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    return

def heater_on_off(value):
    if value is True:
        GPIO.output(11, 1)
        print("Heater ON")
        
    else:
        GPIO.output(11, 0)
        print("Heater OFF")
    return