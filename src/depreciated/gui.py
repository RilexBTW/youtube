from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import time
import youtube_dl
import threading



#download variables - DO NOT CHANGE
downloadReady = 0
fileType = ''
fileFormat = ''
format = 'bestaudio/best'
fileOutputName = ''
fileQuality = ''
testvar = ''



class YTDL(App):
    def build(self):
        self.window = GridLayout()
        self.icon = 'logo.png'
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.4)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #add widget to window

        #image widget
        self.window.add_widget(Image(source="logo.png"))

        #Label widget
        self.greeting = Label(
                        text = "YouTube Downloader",
                        font_size = 38,
                        color ='b3e5fc',
                         font_family = 'Calibri'
                        )

        self.window.add_widget(self.greeting)


        #Mp3 Button
        self.selbutton = Button(
                         text ="MP3",
                         size_hint = (0.,0.5),
                         bold = True,
                         background_color = '#0096FF',
                         font_family = 'Calibri'
                         )
        self.window.add_widget(self.selbutton)
        self.selbutton.bind(on_press=self.mp3)

        #Mp4 button
        self.selbutton2 = Button(
                          text ="MP4",
                          size_hint = (0.1,0.5),
                          bold = True,
                          background_color = '#0096FF',
                          font_family = 'Calibri'
                          )

        self.window.add_widget(self.selbutton2)
        self.selbutton2.bind(on_press=self.mp4)



        # text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y= (0.5,0.5),
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


    def mp3(self,instance): #mp3 callback
        global mp3
        mp3 = 1
        global mp4
        mp4 = 0
        print('[+] Debugging File Type:' + " " + 'MP3')
        print('[+] Debugging file Format:' + " " + 'MP3')
        if downloadReady == 1:
            print('Starting download...')

    def mp4(self,instance): # mp4 callback
        global mp4
        mp4 = 1
        global mp3
        mp3 = 0
        print('[+] Debugging file Format:' + " " + 'MP4')
        print('[+] Debugging File Type:' + " " + 'MP4')


    def callback(self,instance):   ## combined download and gui into one file for simplicity
        downloadReady = 1
        self.greeting.text = "Downloading " + self.user.text + "!"
        url = self.user.text
        time.sleep(2)
        if downloadReady == 0:
            print('awaiting URL...')


        if downloadReady == 1:
            print('Starting download...')

        if mp4 == 1:
            global ydl_opts
            ydl_opts = {
                'format': 'best[ext=mp4]' #137 is 1080, 136 is 720
                    }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        if mp3 == 1:
            global ydl_opts_mp3
            ydl_opts_mp3 = {
                'format': format,
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality': '192',
                        }]
                    }


            with youtube_dl.YoutubeDL(ydl_opts_mp3) as ydl:
                ydl.download([url])
        print("placeholder placeholder placeholder")
        self.greeting.text = "Download Complete!"




        #return self.window






def postDownload(): ## what happens after user decides continue after successful download
    print ("[+] Debug Message: Starting postDownload Function")
    self.greeting.text = "Start another download?"


if __name__ == "__main__":
    YTDL().run()
