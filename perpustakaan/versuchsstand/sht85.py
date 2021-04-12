import os
import time


def read_ambient_values(bus_i2c):
    bus_i2c.write_i2c_block_data(0x44, 0x24, [0x00])
    time.sleep(0.5)
    data = bus_i2c.read_i2c_block_data(0x44, 0x00, 6)

    temp = data[0] * 256 + data[1]
    ctemp = -45 + (175 * temp / 65535.0)
    ftemp = -49 + (315 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

    return ctemp, humidity