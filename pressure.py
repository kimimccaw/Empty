import spidev
import time
import os
import math
import minimalmodbus
import serial
import smbus
import RPi.GPIO as GPIO
import threading

from kivy.clock import Clock

class MyPressure:

    def __init__(self):
        self.update_thread = None
        self.init_adc()
        self.pressure = None
        Clock.schedule_interval(self.start_thread, 1.5)
        
        return
    
    def start_thread(self, dt):
        if self.update_thread == None:
            self.update_thread = threading.Thread(target= self.update)
            self.update_thread.start()
        else:
            if not self.update_thread.isAlive():
                self.update_thread = threading.Thread(target=self.update)
                self.update_thread.start()
            else:
                print("Update: NOT RUNNING")
        return


    def init_adc(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000
        return

    def init_i2c(self):
        self.bus_i2c = smbus.SMBus(1)
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
        self.pressure = self.read_value(2, 150.0, 0, 1, 1000)
        #abcd = str(format(temperature)
        return


a = MyPressure()
a.update()
print(round(a.pressure,3))

