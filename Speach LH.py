import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch ("SAPI.SpVoice")

speak.Speak ("What's your name?")
answer = pg.prompt("Enter your name.")

if answer == "Lauren":
    speak.Speak ("Hello" + answer + " nice to meet your.")

elif answer == "Ella":
    speak.Speak ("Hello" + answer + " it's you I've been looking for.")

elif answer == "Mercy":
    speak.Speak ("Hello" + answer + " Christmas is coming.")

elif answer == "EC":
    speak.Speak ("Hello" + answer + " is Mo your daddy?.")

else:
    speak.Speak ("Nice to meet you!")

speak.Speak ("What's your favorite TV show??")
food = pg.promt("Enter your favorite TV show")

if show == "New Girl or How I Met Your Mother":
    speak.Speak("No way! Me too!")
    wb.open ("https://www.youtube.com/results?search_query="+show)

elif show == "The Office":
    speak.Speak("BOOO!")
    wb.open ("https://www.youtube.com/results?search_query="+crowdbooing)


    
