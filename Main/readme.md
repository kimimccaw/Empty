#Introduction
versuchsstand: Python implementation for the testing platform of the newly developed sensor by IMKO Micromodultechnik.
**This package has been tested on the Raspberry Pi, thus you will find some package is only applicable on the Raspberry Pi**
==================================================================

-------------
##Requirements
-------------

Before you can start using the verscuchsstand software you have to make sure,
that you have at least the following software packages installed.

1. Python (http://python.org)
2. PySerial (http://pyserial.sourceforge.net)
3. minimalmodbus (https://pypi.org/project/minimalmodbus/)
4. implib2 (https://pypi.org/project/IMPLib2/)
5. smbus (https://pypi.org/project/smbus2/)
6. RPi.GPIO (https://pypi.org/project/RPi.GPIO/)


For instructions on how to get and install these packages on your OS
please head over to the official project pages.

##Installation
------------

Install the stable branch using pip::

    pip install versuchsstand

Depending on your system you may have to prefix these commands with ``sudo``!

##Quick Start Manual
------------------

This small quick start manual is intended to give you a basic example of how to use this library. You can use these command or just run the test_package.py

After successfully installing the package and connecting start the python Shell within your terminal::
    $ python
    Python 3.6.2 (default, Jul 17 2017, 16:44:45)
    [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Import the versuchsstand module::
    
    >>> import versuchsstand

Testing the Endress + Hauser group's equipment i.e. Cerabar, Promass, Thermophant::
    
    >>> spi = mcp3008.init_adc()
    >>> print("temperature: ",thermophant.read_value(spi))
    temperature: 21.530277
    >>> print("pressure: ",cerabar.read_value(spi))
    pressure: 0.032209
    >>> print("flow velocity: ",promass.read_value(spi))
    flow velocity: -0.002397

Testing the ambient sensor::
    
    >>> i2c_bus = i2c_bus.init_i2c()
    >>> print("ambient temperature, humidity : ",sht85.read_ambient_values(i2c_bus))
    ambient temperature, humidity : 

Testing the trime sensor::
    
    >>> bus_trime = trime.init_trime()
    >>> moisture = trime.read_sensor(bus_trime)
    >>> print("Moisture: ", moisture)
    Moisture: 

Testing the heater::
    
    >>> heater.init_heater()
    >>> ##to turn on the heater give True in the parameter.
    >>> heater.heater_on_off(True)
    Heater ON
    >>> ##to turn on the heater give False in the parameter.
    >>> heater.heater_on_off(False)
    Heater OFF

Testing the pump::
    
    >>> instrument = modbus.init_pump()
    >>> #turning on the pump
    >>> pump.pump_on_off(instrument,True)
    Pump ON
    >>> #run the pump at specific frequency
    >>> pump.pump_set_frequency(instrument,150)
    >>> #turning off the pump
    >>> pump.pump_on_off(instrument,False)
    Pump OFF



