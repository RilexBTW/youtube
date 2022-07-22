from __future__ import unicode_literals
import youtube_dl



url = ''
fileType = ''
fileFormat = ''
fileOutputName = ''
fileQuality = ''
testvar = ''
downloadReady = ''




class download():
    def grab():
        if downloadReady == 0:
            print('awaiting URL...')


        if downloadReady == 1:
            print('Starting download...')
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        print("placeholder placeholder placeholder")


    grab()






if __name__ == "__main__":
    download()
