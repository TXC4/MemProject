#import kivy
#kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
import random

Builder.load_string("""
<HomeScreen>:
    Label: 
        text: "Welcome!"
<NumbersScreen>:
    GridLayout:
        rows: 2
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            Label:
                id: numLabel
                text: "Number"
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]
                padding_x: 10
        Label:
            id: timeLabel
            text: root.timeNum
    GridLayout:
        cols: 2
        size_hint: 1, .2
        Button:
            text: "New Number"
            on_press: root.getNumbers(2, 1000)
            on_press: root.startTime()
            on_press: root.timeInt = 0
        Button:
            text: "Stop"
            on_press: root.stopTime()
<CardsScreen>:
    GridLayout:
        cols: 1
        Label:
            text: "Screen 2"
<Screen3>:
    Label:
        text: "Screen 3"
<Screen4>:
    Label:
        text: "Screen 4"
<Screen5>:
    Label:
        text: "Screen 5"
<MyApp>:
    rows: 2
    size_hint: 1, .9
    ScreenSwitcher:
        id: manager

    GridLayout:
        cols: 5
        size_hint: 1, .1
        Button:
            text: "1"
            #'ns' is declared in python ScreenSwitcher class
            on_press: root.ids.manager.current = 'ns'
        Button:
            text: "2"
            on_press: root.ids.manager.current = 'cs'
        Button:
            text: "3"
            on_press: root.ids.manager.current = 's3'
        Button:
            text: "4"
            on_press: root.ids.manager.current = 's4'
        Button:
            text: "5"
            on_press: root.ids.manager.current = 's5'
""")
class ScreenSwitcher(ScreenManager):
    def __init__(self,**kwargs):
        super(ScreenSwitcher, self).__init__(**kwargs)
        self.add_widget(HomeScreen(name='hs'))
        self.add_widget(NumbersScreen(name='ns'))
        self.add_widget(CardsScreen(name='cs'))
        self.add_widget(Screen3(name='s3'))
        self.add_widget(Screen4(name='s4'))
        self.add_widget(Screen5(name='s5'))
class HomeScreen(Screen):
    pass
class NumbersScreen(Screen, GridLayout):
    timeNum = StringProperty()
    timeInt = 0
    def increment_time(self, interval):
        if (self.timeInt == 0):
            self.timeNum = '0'
        self.timeInt += 1
        if (self.timeInt < 60):
            self.timeNum = str(round(self.timeInt))
        elif (self.timeInt >= 60):
            self.timeNum = str(round(self.timeInt/60)) + "m " + str(round(self.timeInt%60)) + "s"
    def startTime(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, 1)
    def stopTime(self):
        Clock.unschedule(self.increment_time)
    def getRand(self):
        x = random.randint(0,9)
        return str(x)
    def getNumbers(self, groupSize, quantity):
        x = ""
        for i in range(quantity):
            if (i != 0) & ((i % groupSize) == 0):
                x += " "
            x += self.getRand()
        self.ids.numLabel.text = x
        
class CardsScreen(Screen, GridLayout):
    pass
class Screen3(Screen):
    pass
class Screen4(Screen):
    pass
class Screen5(Screen):
    pass

class MyApp(App, GridLayout):
    def build(self):
        return self

if __name__ == '__main__':
    MyApp().run()