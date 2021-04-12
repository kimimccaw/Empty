import time
import csv
#import pandas as pd
import requests
import os 
from time import strftime, localtime
from versuchsstand import cerabar, heater, i2c_bus, mcp3008, modbus, promass, pump, sht85, thermophant, trime


def record_data(record_time, time_interval, pump_frequency, heat):

    #initializing versuchsstand component
    spi = mcp3008.init_adc()
    bus_i2c = i2c_bus.init_i2c()
    bus_trime = trime.init_trime()

    #initializing versuchsstand actuators
    instrument = modbus.init_pump()
    pump.pump_on_off(instrument,True)
    heater.init_heater()
    heater.heater_on_off(heat)


    #starting recording procedure
    cwd = os.getcwd()
    masa = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    file_name = 'versuchsstand.csv'
    path_csv = os.path.join(cwd, file_name)
    path_xlsx = os.path.join(cwd, 'versuchsstand.xlsx')


    with open( path_csv , 'w', newline='') as f:    
        fieldnames = ['Time', 'Pump frequency', 'Thermophant reading', 'Cerabar reading', 'Promass reading', 'Ambient reading', 'Trime sensor reading' ]
        thewriter = csv.DictWriter(f, fieldnames= fieldnames)


        thewriter.writeheader()
        for i in range(int(record_time/time_interval)) :
            time.sleep(time_interval)
            thewriter.writerow({'Time': strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()),'Pump frequency': pump_frequency ,
                                'Thermophant reading' : thermophant.read_value(spi), 'Cerabar reading' : cerabar.read_value(spi),
                                'Promass reading': promass.read_value(spi) ,'Ambient reading':sht85.read_ambient_values(i2c_bus),
                                'Trime sensor reading': trime.read_sensor(bus_trime)})
            pump.pump_set_frequency(instrument,pump_frequency)

    #turning off the actuator
    pump.pump_set_frequency(instrument,0)
    time.sleep(5)
    pump.pump_on_off(instrument,False)
    
    if heat is True:
        heater.heater_on_off(False)
    else:
        return    
    

    #df = pd.read_csv(path_csv)
    #writer = pd.ExcelWriter(path_xlsx)
    #df.to_excel(writer, index = False)
    #writer.save()


    chat_id = '-441623220'
    files = {'document' : open(path_csv, 'rb')}
    base_Document = 'https://api.telegram.org/bot1434204376:AAH275V5dKSTfiVDzzKE122T05t7f7Cosc0/sendDocument?chat_id={}&caption="{}"'.format(chat_id,masa)
    requests.post(base_Document, files = files)
    pump.pump_on_off(instrument,False)


    print('Operation complete')


#record_data(60,5)


