#this script is bus protocol for the pump

import os
import minimalmodbus
import serial


def init_pump():
    #20: bus address
    instrument = minimalmodbus.Instrument('/dev/ttyUSB_PUMP', 20)
    instrument.serial.baudrate = 9600
    instrument.serial.parity = serial.PARITY_NONE
    instrument.serial.timeout = 5
    instrument.debug = False
    return instrument

