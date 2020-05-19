#import kivy
#kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, WipeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
import random

Builder.load_string("""
<HomeScreen>:
    Label: 
        text: "Welcome!"
<NumbersScreen>:
    GridLayout:
        rows: 2
        size_hint: 1, .85
        pos_hint: {"top" : .85}
        Label:
            id: timeLabel
            text: root.timeNum
            size_hint_y: .1
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            Label:
                id: numLabel
                text: "Press Start to begin.\\n\\n-Generates random digits to practice memorization.\\n-You may customize quantity, group, and base."
                font_size: "20sp"
                halign: "center"
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]
                padding_x: 10
                padding_y: 10
        
    GridLayout:
        cols: 5
        size_hint: 1, .15
        pos_hint: {"top" : 1}
        Button:
            font_size: "14sp"
            text: "Start\\nReset"
            on_release: root.newNums()
            on_release: root.startTime()
            on_release: root.timeInt = 0
        Button:
            font_size: "14sp"
            text: "Stop"
            on_release: root.stopTime()
        Spinner:
            font_size: "14sp"
            text: "Quantity"
            values: ('3','5','10','15','20','25','50','100','250','500','1000','2500','5000','10000')
            on_text: root.printv(self.text), root.setQuantity(self.text)
        Spinner:
            font_size: "14sp"
            text: "Grouping"
            values: ('None','1', '2','3','4','5','10')
            on_text: root.printv(self.text), root.setGrouping(self.text)
        Spinner:
            font_size: "14sp"
            text: "Base"
            values: ('Binary', 'Base 10', 'Hex')
            on_text: root.printv(self.text)
                
    
<CardsScreen>:
    canvas.before:
        Color:
            rgba: .14,.40,.20,1
        Rectangle:
            pos: app.pos
            size: app.size
    GridLayout:
        rows:1
        size_hint: 1,1
        Label:
            text: "Press Shuffle to begin.\\n-Swipe right for next card\\n-Swipe left for previous card\\n-You may customize the number of cards or number of decks."
            font_size: "20sp"
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
            padding_x: 10
            padding_y: 10  

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
    ScreenSwitcher:
        id: manager
        size_hint: 1, .9
        pos_hint: {"top" : 1}
    GridLayout:
        cols: 5
        size_hint: 1, .1
        Button:
            font_size: "12sp"
            text: "numbers"
            #'ns' is declared in python ScreenSwitcher class
            on_release: root.ids.manager.current = 'ns'
        Button:
            font_size: "12sp"
            text: "cards"
            on_release: root.ids.manager.current = 'cs'
        Button:
            text: "3"
            on_release: root.ids.manager.current = 's3'
        Button:
            text: "4"
            on_release: root.ids.manager.current = 's4'
        Button:
            text: "5"
            on_release: root.ids.manager.current = 's5'
""")


########################################################################################
########################################################################################
########################################################################################

class ScreenSwitcher(ScreenManager):
    def __init__(self,**kwargs):
        super(ScreenSwitcher, self).__init__(**kwargs,  transition=WipeTransition())
        self.add_widget(HomeScreen(name='hs'))
        self.add_widget(NumbersScreen(name='ns'))
        self.add_widget(CardsScreen(name='cs'))
        self.add_widget(Screen3(name='s3'))
        self.add_widget(Screen4(name='s4'))
        self.add_widget(Screen5(name='s5'))
class HomeScreen(Screen):
    pass
class NumbersScreen(Screen, GridLayout):
    quantity = 25
    grouping = 0
    base = 10
    timeNum = StringProperty()
    timeInt = 0
    def printv(self, x):
        print(x)
    def setQuantity(self, quantity):
        self.quantity = int(quantity)
    def setGrouping(self, grouping):
        if grouping == 'None':
            self.grouping = 0
        else:
            self.grouping = int(grouping)
    def setBase(self, base):
        self.base = int(base)
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
        if groupSize == 0:
            for i in range(quantity):
                x += self.getRand()
        else:
            for i in range(quantity):
                if (i != 0) & ((i % groupSize) == 0):
                    x += " "
                x += self.getRand()
        self.ids.numLabel.text = x
    def newNums(self):
        self.getNumbers(self.grouping, self.quantity)
        
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