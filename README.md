# ytdlgui

GUI Wrapper written in python for YouTubeDL

Currently Installation from Source is the only supported way to install until an official alpha is released.

## Installation from source - Run from folder
```console
# clone the repo
$ git clone https://www.github.com/rilexbtw/youtube.git

# navigate to the youtube directory
$ cd youtube

# install the requirements
$ python3 -m pip install -r requirements.txt
```
## Build executable from source

```console
# clone the repo
$ git clone https://www.github.com/rilexbtw/youtube.git

# navigate to the youtube directory
$ cd youtube

# install the requirements
$ python3 -m pip install -r requirements.txt

# install pyinstaller to build
$ pip install pyinstaller

# compile the executable
$ pyinstaller ytdl.spec --clean
```


# Changelog:

# 1.0.0.-a0.4
# Changed
- Reorganized file structure into src folder

# Added
- Build instructions to README file for anyone who doesn't want to run a random EXE

# 1.0.0-a0.3
## Changed
- Reworked entire UI (again)
- Created a more official app Icon
- Renamed guirevised to app.py

## Fixed
- Fixed mp3 and mp4 not working after moving to the gui revised variant

## Added
- Started building update.py script

## Notes
in order to fix ffmpeg error, installed ffmpeg exe files to 'C:\\Users\\%user%\\AppData\\Local\\Programs\\Python310\\Scripts'

It's still unclear if the update.py script will be standalone or an integrated function. The main functionality I seek at the moment is to allow users an optional streamlined or automatic update / upgrade path without the need to go to github and download the newest version. This of course will allow for security and bug fixes to be automatically installed which ideally will make the overall experience better. Obviously with automatic updates things can end up breaking or not working when they worked in an earlier version which is one of the reasons why this will remain an optional feature and it is also a reason why it will only pull updates from release versions, not the updated source code

In its current state, this project should be seeing an alpha release fairly soon :)




# 1.0.0-a0.2
## Added
- App Icon (Temp Image)

## Fixed
- Bugs where mp3 and mp4 would glitch each other

## Notes
- mp3 and mp4 now work, although the cosmetics need a lot of work



# 1.0.0-a0.1
## Added
- Base GUI
- Base download functionality

## Changed
- Merged all files into one file (GUI.py)


## Notes
- Current functionality works as follows. Run gui.py, enter video url, press download and the download will start.

## YTDL GUI Roadmap

 - Add Support for all YouTubeDL / FFMPEG functions while remaining simplistic and easy to user
 - Create an update utility as an optional function to assist non tech savvy users
 - Create an executable file for Windows Users so dependencies aren't needed to use / install
 - Create a Download History list
 - Show output of terminal in application window instead of using a terminal
