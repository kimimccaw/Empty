import spidev
import time
import os
import math
import minimalmodbus
import serial
import smbus
import RPi.GPIO as GPIO
import threading
import datetime

from kivy.clock import Clock

class MyTemp:

    def __init__(self):
        self.update_thread = None
        self.init_adc()
        self.temperature = None
        self.outSheet = None
        self.nilai = []
        self.tarikh = []
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
        self.temperature = self.read_value(0, 131.3, 0, 150, 1000)
        #abcd = str(format(temperature)
        return

    #def create_excel(self,date):
    #    self.outWorkbook = xlsxwriter.Workbook("temperature"+str(date)+".xlsx")
    #    self.outSheet = self.outWorkbook.add_worksheet()
    #    self.outSheet.write("A1", "timestamps")
    #    self.outSheet.write("B1", "temperature")

    #    return

    #def update_excel(self,value,masa):
    #    self.nilai.append(value)
    #    self.tarikh.append(masa)
    #    self.outSheet.write(self.nilai.index(value)+1, 0, value)
    #   self.outSheet.write(self.tarikh.index(masa)+1, 1, masa)



    #    return



#harini = datetime.datetime.now()
a = MyTemp()
a.update()
#a.create_excel(harini.date())
#a.update_excel(a.temperature,harini.time())
print(round(a.temperature,1))

