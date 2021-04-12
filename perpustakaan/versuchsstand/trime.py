## This module is for connection to the trime bus protocol
import implib2


def init_trime():
    bus_trime = implib2.Bus('/dev/ttyUSB_VARIANT')
    bus_trime.sync()
    return bus_trime

#serial_no; 48101: SondeVariant1 , 48102: WickelSonde
def read_sensor(bus_trime, serial_no):
    module = implib2.Module(bus_trime, serial_no)
    module.set_event_mode()
    if module.get_average_mode() is not "CS":
        module.set_average_mode("CS")

    
    moisture = module.get_measurement('Moist')
    transit_time = module.get_measurement('TransitTime')
    pseudo_transit_time = module.get_measurement('PseudoTransitTime')

    return moisture, transit_time, pseudo_transit_time
