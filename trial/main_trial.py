import math
from pressure import MyPressure
from temperature import MyTemp
from volume_velocity import MyVolVel
from viscosity import MyVisc

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

Builder.load_file('main.kv')

class Test(TabbedPanel):
    pass


class MyApp(App):

    def build(self):
        self.test = Test()
        Clock.schedule_interval(self.updatelol, 1)
        return self.test

    def updatelol(self,dt):

        press = MyPressure()
        temp = MyTemp()
        vel = MyVolVel()
        visc = MyVisc()

        press.update()
        temp.update()
        vel.update()
        visc.update()

        #unit of volume velocity is m3/h
        #radius = 0.0142 m
        flow_velocity = (vel.volume_velocity / 3600) / (math.pi * 0.0142 * 0.0142)
        self.test.ids.label_text_temperature.text = "[color=ef9121][b]" + str(format(temp.temperature, '.2f')) + "[/b]" + " °C[/color]"
        self.test.ids.label_text_pressure.text = "[color=ef9121][b]" + str(format(press.pressure, '.2f')) + "[/b]" + " Pa[/color]"
        self.test.ids.label_text_viscosity.text = "[color=ef9121][b]" + str(format(visc.viscosity, '.2f')) + "[/b]" + " cP[/color]"
        self.test.ids.label_text_flow_velocity.text = "[color=ef9121][b]" + str(format(flow_velocity, '.2f')) + "[/b]" + " m/s[/color]"
        
        return


if __name__ == '__main__':
    MyApp().run()

        
