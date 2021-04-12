import time
from versuchsstand import mcp3008,thermophant,cerabar,i2c_bus
from versuchsstand import heater,promass,sht85,modbus,pump,trime


##testing the cerabar, thermophant and promass

spi = mcp3008.init_adc()
print("temperature: ",thermophant.read_value(spi))
print("pressure: ",cerabar.read_value(spi))
print("flow velocity: ",promass.read_value(spi))


##testing the ambient sensor

i2c_bus = i2c_bus.init_i2c()
print("ambient temperature, humidity : ",sht85.read_ambient_values(i2c_bus))


##testing the trime sensor

bus_trime = trime.init_trime()
moisture = trime.read_sensor(bus_trime)
print("Moisture: ", moisture)


##testing the heater

heater.init_heater()
##to turn on the heater give 1 in the parameter.
heater.heater_on_off(True)
timer = 20
while timer:
    time.sleep(1)
    timer-= 1

##to turn off the heater give 0 in the parameter
heater.heater_on_off(False)


##testing the pump

#turning on the pump
instrument = modbus.init_pump()
pump.pump_on_off(instrument,True)

##running the pump at a specific frequency for 20 seconds
pump.pump_set_frequency(instrument,150)
timer = 20
while timer:
    time.sleep(1)
    timer-= 1

#turning of the pump
pump.pump_on_off(instrument,False)

