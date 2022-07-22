from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

logo = 'logo.png'

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.add_widget(Image(source=logo))
        #Label widget
        self.greeting = Label(text="What's your name?")
        self.window.add_widget(self.greeting)
        # text input widget
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)






        return self.window

if __name__ == "__main__":
    SayHello().run()
