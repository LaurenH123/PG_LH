import pyautogui as pg
import time

pg.hotkey("winleft","ctrl","d")
pg.hotkey("winleft")
pg.typewrite("chrome\n",0.3)
pg.hotkey("winleft","up")
time.sleep(1)
pg.hotkey("winleft","up")
time.sleep(1)
pg.hotkey("winleft","up")
time.sleep(1)
pg.typewrite("https://www.youtube.com/watch?v=yqEeP1acj4Y\n",0.1)
time.sleep(1)
pg.hotkey("f")
time.sleep(1.24)
pg.hotkey("esc")
pg.typewrite("https://www.youtube.com/watch?v=J0BWUqBkkVE\n",0.1)
time.sleep(1)
pg.hotkey("f")
time.sleep(1.24)
