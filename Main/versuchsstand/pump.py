import os


def pump_on_off(instrument, value):
    if value is True:
        instrument.write_register(2001, 1119)
        print("Pump ON")
    else:
        instrument.write_register(2001, 1118)
        print("Pump OFF")
    return

def pump_set_frequency(instrument, frequency):
    if frequency > 0:
        instrument.write_register(2002, frequency)
    return
