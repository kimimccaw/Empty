#package for i2c bus
#i2c bus is bus protocol for the ambient sensor
import smbus


def init_i2c():
    bus_i2c = smbus.SMBus(1)
    return bus_i2c