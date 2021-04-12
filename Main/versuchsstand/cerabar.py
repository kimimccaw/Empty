#package for the pressure measurement equipment

import os


def read_channel(spi, channel):
    # Function to read SPI data from MCP3008 chip
    # Channel must be an integer 0-7
    adc = spi.xfer2([1, (8 + channel) << 4, 0 ])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def read_value(spi):

    # hardware parameters
    channel = 2
    resistance = 150.0
    lower_limit = 0
    upper_limit = 1
    loop = 1000

    if loop > 0:
        average = 0
        for i in range(loop):
            adc = read_channel(spi, channel)
            voltage = (adc / 1023.0) * 3.3
            current = (voltage/resistance) * 1000
            result = (((current - 4.0) / (20.0 - 4.0)) * (upper_limit - lower_limit)) + lower_limit
            average += result / float(loop)       
    else:
        return
        
    return average