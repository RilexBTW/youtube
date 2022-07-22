from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #add widget to window

        #image widget
        self.window.add_widget(Image(source="logo.png"))

        #Label widget
        self.greeting = Label(
                        text ="What Would You Like to Download Today??",
                        font_size = 38,
                        color ='#0096FF'
                        )

        self.window.add_widget(self.greeting)

        #Url widget
        self.subgreeting = Label(
                           text ="Paste URL here",
                           font_size = 24,
                           color = '000080'
                           )
        self.window.add_widget(self.subgreeting)


        # text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y= (20,20),
                    size_hint = (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # Button widget
        self.button = Button(
                      text="Download!",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color ='#0096FF'
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self,instance):
        self.greeting.text = "Downloading " + self.user.text + "!"

        return self.window

if __name__ == "__main__":
    SayHello().run()
