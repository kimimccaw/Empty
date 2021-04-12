from versuchsstand import mcp3008,thermophant,cerabar,i2c_bus,promass,sht85


# init spi
spi = mcp3008.init_adc()
i2c_bus = i2c_bus.init_i2c()
print("temperature: ",thermophant.read_value(spi))
print("pressure: ",cerabar.read_value(spi))
print("flow velocity: ",promass.read_value(spi))

print("ambient temperature, humidity : ",sht85.read_ambient_values(i2c_bus))

