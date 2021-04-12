import spidev
import time
import os
import math


class MyVolVel:

    def __init__(self):
        self.init_adc()
        self.volume_velocity = None
        return

    def init_adc(self):
        # Open SPI bus
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        return

    def read_channel(self, channel):
        # Function to read SPI data from MCP3008 chip
        # Channel must be an integer 0-7
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0 ])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def read_value(self, channel, resistance, lower_limit, upper_limit, loop = 1):

        if loop > 0:
            average = 0
            for i in range(loop):
                adc = self.read_channel(channel)
                voltage = (adc / 1023.0) * 3.3
                current = (voltage/resistance) * 1000
                result = (((current - 4.0) / (20.0 - 4.0)) * (upper_limit - lower_limit)) + lower_limit
                average += result / float(loop)
        
        else:
            return
        
        return average

    def update(self):
        self.volume_velocity = self.read_value(4, 150.0, 0, 4, 1000)
        return


