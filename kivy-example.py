#import kivy
#kivy.require('1.11.1') # replace with your current kivy version !

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, CardTransition
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
        size_hint: 1, .9
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
        size_hint: 1, .1
        pos_hint: {"top" : 1}
        Button:
            font_size: "14sp"
            text: "Start\\nReset"
            background_color: [.421,.929,.464,1]
            on_release: root.newNums()
            on_release: root.startTime()
            on_release: root.timeInt = 0
        Button:
            font_size: "14sp"
            text: "Stop"
            background_color: [.945,.246,.246,1]
            on_release: root.stopTime()
        GridLayout:
            rows: 2
            Label:
                text: "Quantity"
            Spinner:
                font_size: "14sp"
                text: str(root.quantity)
                values: ('3','5','10','15','20','25','50','100','250','500','1000','2500','5000','10000')
                on_text: root.printv(self.text), root.setQuantity(self.text)
        GridLayout:
            rows: 2
            Label:
                text: "Grouping"
            Spinner:
                font_size: "14sp"
                text: 'None'
                values: ('None','1', '2','3','4','5','8','10', 'Phone #')
                on_text: root.printv(self.text), root.setGrouping(self.text)
        GridLayout:
            rows: 2
            Label:
                text: "Base"
            Spinner:
                font_size: "14sp"
                text: root.base
                values: ('Base 10', 'Binary')
                on_text: root.printv(self.text), root.setBase(self.text)
    
<CardsScreen>:
    canvas.before:
        Color:
            rgba: .14,.40,.20,1
        Rectangle:
            pos: app.pos
            size: app.size
    GridLayout:
        rows:2
        size_hint: 1,1
        GridLayout:
            cols: 5
            size_hint_y: .1
            pos_hint: {"top" : 1}
            Button:
                text: 'Prev'
                background_color: (.297, .297, .297, 1)
            Button:
                text: 'Shuffle'
                on_release: root.shuffleCards(root.quantity, root.grouping)
            GridLayout:
                rows: 2
                Label:
                    size_hint_y: .5
                    text: 'Quantity'
                Spinner:
                    text: str(root.quantity)
                    font_size: "14sp"
                    values: ('1', '2', '3', '5', '10', '20', '30', '52')
            GridLayout:
                rows: 2
                Label:
                    size_hint_y: .5
                    text: 'Grouping'
                Spinner:
                    text: root.grouping
                    font_size: "14sp"
                    values: ('Cards', 'Pairs', 'Hands', 'Decks')
            Button:
                text: 'Next'
                background_color: (.297, .297, .297, 1)
                on_release: root.getNextCard()
        CardScreenSwitcher:
            id: cardScreenManager
            size_hint_y: .8
            pos_hint: {"top" : .9}
<CardInstructionsScreen>:
    Label:
        text: "Instructions"
<CardGameScreen>:
    GridLayout:
        rows: 3
        Label:
            size_hint_y: .1
            text: "Time Elapsed"
        Image:
            id: cardImg
        Label:
            size_hint_y: .1
            text: "Card Num / Total"

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
            on_release: root.ids.manager.current = 'ns'
            background_color: (.297, .297, .297, 1)
        Button:
            font_size: "12sp"
            text: "cards"
            on_release: root.ids.manager.current = 'cs'
            background_color: (.297, .297, .297, 1)
        Button:
            text: "3"
            on_release: root.ids.manager.current = 's3'
            background_color: (.297, .297, .297, 1)
        Button:
            text: "4"
            on_release: root.ids.manager.current = 's4'
            background_color: (.297, .297, .297, 1)
        Button:
            text: "5"
            on_release: root.ids.manager.current = 's5'
            background_color: (.297, .297, .297, 1)
""")


########################################################################################
########################################################################################
########################################################################################

class ScreenSwitcher(ScreenManager):
    def __init__(self,**kwargs):
        super(ScreenSwitcher, self).__init__(**kwargs,  transition=FadeTransition())
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
    base = 'Base 10'
    timeNum = StringProperty()
    timeInt = 0
    def printv(self, x):
        print(x)
    def setQuantity(self, quantity):
        self.quantity = int(quantity)
    def setGrouping(self, grouping):
        if grouping == 'None':
            self.grouping = 0
        elif grouping == 'Phone #':
            self.grouping = -1
        else:
            self.grouping = int(grouping)
    def setBase(self, base):
        self.base = base
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
        if self.base == 'Base 10':
            x = random.randint(0,9)
        elif self.base == 'Binary':
            x = random.randint(0,1)
        return str(x)
    def getNumbers(self, grouping, quantity):
        x = ""
        if grouping == 0:
            for i in range(quantity):
                x += self.getRand()
        elif grouping == -1: #phone numbers
            for i in range(quantity):
                x += '('
                for j in range(3):
                    x += self.getRand()
                x += ')'
                for j in range(3):
                    x += self.getRand()
                x += '-'
                for j in range(4):
                    x += self.getRand()
                x += "   "
        else:
            for i in range(quantity):
                if (i != 0) & ((i % grouping) == 0):
                    x += " "
                x += self.getRand()
        self.ids.numLabel.text = x
    def newNums(self):
        self.getNumbers(self.grouping, self.quantity)
        
class CardsScreen(Screen, GridLayout):
    quantity = 10
    grouping = 'Cards'
    currentCard = 0
    totalCards = 0
    cardScreenList = []
    cardImageList = ["c01.png","c02.png","c03.png","c04.png","c05.png","c06.png","c07.png","c08.png","c09.png","c10.png","c11.png","c12.png","c13.png",
    "d01.png","d02.png","d03.png","d04.png","d05.png","d06.png","d07.png","d08.png","d09.png","d10.png","d11.png","d12.png","d13.png",
    "h01.png","h02.png","h03.png","h04.png","h05.png","h06.png","h07.png","h08.png","h09.png","h10.png","h11.png","h12.png","h13.png",
    "s01.png","s02.png","s03.png","s04.png","s05.png","s06.png","s07.png","s08.png","s09.png","s10.png","s11.png","s12.png","s13.png"]

    # keep in bounds
    def getNextCard(self):
        self.currentCard += 1
        self.ids.cardScreenManager.current = 'card' + str(self.currentCard)

    # find why multiple name occurences
    def shuffleCards(self, q, g):
        self.cardScreenList.clear()
        self.ids.cardScreenManager.clear_widgets()
        self.currentCard = 0
        c = 0
        if g == 'Decks':
            c = q * 52
            q = q * 52
        elif g == 'Cards':
            c = q
            q = 52
        self.totalCards = c
        print("c", c, "q", q)
        temp = random.sample(range(q), c)
        for i in range(c):
            print(i, ", ", temp[i] % 52)
            print(self.cardImageList[temp[i] % 52])
            #then create list of screen objects and place those images onto them
            #image screen show should be [0] next button incrs prev decrs
            tempStr = 'card' + str(i)
            self.cardScreenList.append(CardGameScreen(name=tempStr))
            self.cardScreenList[i].ids.cardImg.source = 'Images/Cards/' + self.cardImageList[temp[i] % 52]
            self.ids.cardScreenManager.add_widget(self.cardScreenList[i])
            print(self.cardScreenList[i].name)
        self.ids.cardScreenManager.current = 'card' + str(self.currentCard)
        print("END\n\n")
class CardScreenSwitcher(ScreenManager):
    def __init__(self,**kwargs):
        super(CardScreenSwitcher, self).__init__(**kwargs, transition=CardTransition())
        self.add_widget(CardInstructionsScreen(name='cis'))
class CardInstructionsScreen(Screen):
    pass
class CardGameScreen(Screen):
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