from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import time
import youtube_dl



#download variables
fileType = ''
fileFormat = ''
fileOutputName = ''
fileQuality = ''
testvar = ''
downloadready = ''
debug = print()

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.4)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #add widget to window

        #image widget
        self.window.add_widget(Image(source="logo.png"))

        #Label widget
        self.greeting = Label(
                        text ="What Would You Like to Download Today??",
                        font_size = 38,
                        color ='b3e5fc'
                        )

        self.window.add_widget(self.greeting)



        #Url widget
        self.subgreeting = Label(
                           text ="Paste URL in box below",
                           font_size = 24,
                           color = 'e1f5fe'
                           )
        self.window.add_widget(self.subgreeting)

        self.selbutton = Button(
                         text ="mp3",
                         size_hint = (0.,.5),
                         bold = True
                         )
        self.window.add_widget(self.selbutton)



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





    def callback(self,instance):   ## combined download and gui into one file for simplicity
        downloadReady = 1
        self.greeting.text = "Downloading " + self.user.text + "!"
        url = self.user.text
        time.sleep(2)
        if downloadReady == 0:
            debug('awaiting URL...')


        if downloadReady == 1:
            debug('Starting download...')
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        debug("placeholder placeholder placeholder")




        return self.window






if __name__ == "__main__":
    SayHello().run()
