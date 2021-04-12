#this script is bus protocol connection for the sensors by Endress + Hauser Group
import os
import spidev


def init_adc():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1000000
    return spi
