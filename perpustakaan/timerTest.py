import time
import csv
#import pandas as pd
import requests
import os 
import glob
import versuchsstand
from time import strftime, localtime
from versuchsstand import cerabar, heater, i2c_bus, mcp3008, modbus, promass, pump, sht85, thermophant, trime


def record_data(record_time, time_interval, pump_frequency, heat, remarks):

    #initializing versuchsstand component
    spi = mcp3008.init_adc()
    bus_i2c = i2c_bus.init_i2c()
    bus_trime = trime.init_trime()

    #initializing versuchsstand actuators
    instrument = modbus.init_pump()
    pump.pump_on_off(instrument,True)
    heater.init_heater()
    heater.heater_on_off(heat)
    pump.pump_set_frequency(instrument,30)
    time.sleep(2)
    pump_freq = pump_frequency
    pump.pump_set_frequency(instrument,pump_freq)
    #starting recording procedure
    cwd = os.getcwd()
    masa = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    file_name = 'versuchsstand' + masa + '.csv'
    path_csv = os.path.join(cwd, file_name)
    remove_csv = glob.glob('*.csv')
    for i in remove_csv:
        os.remove(i)
    
    if remarks is None:
        notes = 'No notes'
    else:
        notes = remarks

    #path_xlsx = os.path.join(cwd, 'versuchsstand.xlsx')

    print('Data recording begin')

    with open( path_csv , 'w', newline='') as f:    
        fieldnames = ['Time', 'Pump_frequency', 'Thermophant_reading', 'Cerabar_reading', 'Promass_reading', 'Ambient_temperature', 'Ambient_humidity', 'Trime_moist', 'Trime_transit_time', 'Trime_pseudo_time', 'Trime_moist_1', 'Trime_transit_time_1', 'Trime_pseudo_time_1' ]
        thewriter = csv.DictWriter(f, fieldnames= fieldnames)


        thewriter.writeheader()
        for i in range(int(record_time/time_interval)) :
            time.sleep(time_interval)
            #if pump_freq <= 350 :
            #    pump_freq +=5
            #else:
            #    pump_freq = 100 
            #print(pump_freq)
            pump.pump_set_frequency(instrument,pump_freq)
            try:
                reading = trime.read_sensor(bus_trime,48101)
            except:
                reading = trime.read_sensor(bus_trime,48101)


            try:
                reading_1 = trime.read_sensor(bus_trime,48012)
            except:
                reading_1 = trime.read_sensor(bus_trime,48012)
            
            
            thewriter.writerow({'Time': strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()),'Pump_frequency': pump_freq ,
                                'Thermophant_reading' : thermophant.read_value(spi), 'Cerabar_reading' : cerabar.read_value(spi),
                                'Promass_reading': promass.read_value(spi) ,'Ambient_temperature':sht85.read_ambient_values(bus_i2c)[0], 'Ambient_humidity':sht85.read_ambient_values(bus_i2c)[1],
                                'Trime_moist': reading[0], 'Trime_transit_time': reading[1], 'Trime_pseudo_time': reading[2],  'Trime_moist_1': reading_1[0], 'Trime_transit_time_1': reading_1[1], 'Trime_pseudo_time_1': reading_1[2] })
            

    #turning off the actuator
    time.sleep(3)
    pump.pump_set_frequency(instrument,30)
    time.sleep(3)
    pump.pump_set_frequency(instrument,0)
    time.sleep(3)
    pump.pump_on_off(instrument,False)
    
    if heat is True:
        heater.heater_on_off(False)  
    
    #df = pd.read_csv(path_csv)
    #writer = pd.ExcelWriter(path_xlsx)
    #df.to_excel(writer, index = False)
    #writer.save()


    chat_id = '-441623220'
    files = {'document' : open(path_csv, 'rb')}
    base_Document = 'https://api.telegram.org/bot1434204376:AAH275V5dKSTfiVDzzKE122T05t7f7Cosc0/sendDocument?chat_id={}&caption="{}"'.format(chat_id,(masa + ' remarks: ' + notes))
    requests.post(base_Document, files = files)
    pump.pump_on_off(instrument,False)


    print('Operation complete')


#record_data(60,5)


