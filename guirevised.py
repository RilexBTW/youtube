from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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

url_text_input = ObjectProperty()





class MyFloatLayout(FloatLayout):


    def mp3(self): #mp3 callback
        global mp3
        mp3 = 1
        global mp4
        mp4 = 0
        print('[+] Debugging File Type:' + " " + 'MP3')
        print('[+] Debugging file Format:' + " " + 'MP3')
        if downloadReady == 1:
            print('Starting download...')
            print(f'current url: + {url}')

    def mp4(self): # mp4 callback
        global mp4
        mp4 = 1
        global mp3
        mp3 = 0
        print('[+] Debugging file Format:' + " " + 'MP4')
        print('[+] Debugging File Type:' + " " + 'MP4')
        if downloadReady == 1:
            print('Starting download...')
            print('current url:' + url)

    def downloadCallback(self):   ## combined download and gui into one file for simplicity
        target_url = self.url_text_input.text
        downloadReady = 1
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
                ydl.download([target_url])
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
                ydl.download([target_url])
        print("placeholder placeholder placeholder")
        self.greeting.text = "Download Complete!"




        #return self.window






def postDownload(): ## what happens after user decides continue after successful download
    print ("[+] Debug Message: Starting postDownload Function")
    self.greeting.text = "Start another download?"
    url = ''




class YTDL(App):
    def build(self):
        self.icon = ('logo.png')
        return MyFloatLayout()


if __name__ == "__main__":
    YTDL().run()
