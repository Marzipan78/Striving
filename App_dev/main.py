import kivy
from kivy.app import App
from kivy.uix.label import BoxLayout

kivy.require('1.9.0')

class RandomNumber(App):

    def build(self):
        return BoxLayout()


randomnumber = RandomNumber()