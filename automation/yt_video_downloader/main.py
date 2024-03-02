from pytube import YouTube, exceptions
from sys import argv

try:
    link = argv[1]
except IndexError:
    try:
        link = input("paste a video link here: ")
        print("you must provide link to a video as second parameter")
    except:
        print("wrong input")
        exit()

try:
    yt = YouTube(link)
except exceptions.RegexMatchError:
    print("Couldn't find this video, sorry")
    exit()

print("Title: ",yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('./downloaded')