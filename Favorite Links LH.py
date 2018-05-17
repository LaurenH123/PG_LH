import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=i23aUei_7ig", "https://www.youtube.com/watch?v=BAAtH1HO8L0"]

music = ["https://soundcloud.com/", "https://www.spotify.com/us/"]

tvshows = ["https://www.netflix.com/", "https://www.hulu.com/"]

clothing = ["https://www.brandymelvilleusa.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch funny video?
b) Listen to music?
c) Watch your favorite tvshows?
d) Go online shopping?

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
elif answer == "c":
    for i in tvshows:
        webbrowser.open(i)
elif answer == "d":
    for i in clothing:
        webbrowser.open(i)
