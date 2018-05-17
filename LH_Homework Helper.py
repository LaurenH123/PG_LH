import pyautogui as pg
import webbrowser

Mathassignmentsheet = ["https://docs.google.com/spreadsheets/d/1bE7-_l5PTVw_cI-FmB8PsQd_k6V2r7b9gZPCZIPk0KQ/edit#gid=0"]
Englishassignmentsheet = ["https://docs.google.com/document/d/1YchlqX5JcEXXj1OBtWJRVhWjGqUmua90ChHbWr3vCoY/edit"]
Historyassignmentsheet = ["https://docs.google.com/document/d/1SO0Ak5ix6nhHKSlw3vN_A6ehMkQHKT9dFRKmvSiR3Pk/edit"]

answer = pg.prompt(
"""
Which homework would you rather do?
a) Math
b) English
c) History

"""
    )

if answer == "a":
    for i in Mathassignmentsheet:
        webbrowser.open(i)
elif answer == "b":
    for i in Englishassignmentsheet:
        webbrowser.open(i)
elif answer == "c":
    for i in Historyassignmentsheet:
        webbrowser.open(i)

