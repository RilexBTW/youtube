from __future__ import unicode_literals
import youtube_dl



url = 'https://www.youtube.com/watch?v=pwBFOuCrdr4'
fileType = ''
fileFormat = ''
fileOutputName = ''
fileQuality = ''
testvar = ''




class download():
    def grab():
        print('Starting download...')
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    print("placeholder placeholder placeholder")
    grab()






if __name__ == "__main__":
    download()
