from RPi.GPIO import GPIO


def init_heater():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    return