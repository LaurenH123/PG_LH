import pyautogui as pg
import webbrowser
import time

hunger = pg.prompt(
    """
How would you describe you hunger?
a)Hungry
b)Not Very Hungry
c)Full

""")

if hunger == "a":
    meal = pg.prompt(
        """
What type of meal do you want?
a)Breafast
b)Lunch
c)Dinner 
""")
    if meal == "a":
        restaurant = pg.prompt(
            """
Where would you rather go to for Breakfast?
a) le pain quotidien
b) glory days diner
c) Granola Bar
""")
        if restaurant == "a":
            webbrowser.open("https://www.ezcater.com/sem/brand/le-pain-quotidien?mcx=gf1&utm_source=google&utm_medium=cpc&utm_term=le%20pain%20quotidien&utm_content=261508576950&utm_campaign=288499498&utm_adgroup=41272904593&utm_account_id=6262417583&utm_geo=9003435&utm_matchtype=e&utm_device=c&utm_upload_version=1&utm_keyword_format=manual-e1&utm_exprt=&utm_exprt_ad=100-catering-menu&utm_account=National-Manual&gclid=EAIaIQobChMI4_nC74LY2gIVCz0MCh2zyAlNEAAYASAAEgI1zvD_BwE")
        elif restaurant == "b":
            webbrowser.open("http://www.glorydaysdiner.com/")
        elif restaurant == "c":
            webbrowser.open("https://thegranolabarct.com/")

    if meal == "b":
        restaurant = pg.prompt(
            """
Where would you rather go for Lunch?
a) Meli Melo
b) Asiana
c) Chipotle
""")
        if restaurant == "a":
            webbrowser.open("http://www.melimelogreenwich.com/")
        elif restaurant == "b":
            webbrowser.open("http://www.asianacafe.com/")
        elif restaurant == "c":
            webbrowser.open("https://www.chipotle.com/")

    elif meal == "c":
        restaurant = pg.prompt(
            """
Where would you rather go for Dinner?
a) Terra
b) Medditeranio
c) Harvest
""")
        if restaurant == "a":
            webbrowser.open("http://www.zhospitalitygroup.com/terra/")
        elif restaurant == "b":
            webbrowser.open("http://www.zhospitalitygroup.com/mediterraneogreenwich/")
        elif restaurant == "c":
            webbrowser.open("https://harvestwinebar.com/")


elif hunger == "b":
    snack = pg.prompt(
        """
What type of snack do you want? 
a)Ice cream: Pinkberry
b)Coffe/Bakes Goods: Starbucks  
c)Smoothies: Green and Tonic 
""")
    if snack == "a":
        webbrowser.open("http://www.pinkberry.com/loyalty/#mobileapp_bottom")
    elif snack == "b":
        webbrowser.open("https://www.starbucks.com/menu?&utm_term=starbucks&gclid=EAIaIQobChMI_4jP3ITY2gIVi56fCh3TNQW5EAAYASAAEgLFkfD_BwE&cm_mmc=google-_-BR+-+Brand+-+Starbucks+-+Desktop+-+Exact-_-Brand+-+Starbucks+-+Desktop+-+Exact-_-starbucks_mkwid%7CswofCu5MS_dc%7Cpcrid%7C202075197264%7Cpkw%7Cstarbucks%7Cpmt%7Ce&utm_campaign=BR+-+Brand+-+Starbucks+-+Desktop+-+Exact&utm_medium=cpc&utm_source=google")
    elif snack == "c":
        webbrowser.open("http://greenandtonic.com/")
    
    
elif hunger == "c":
   pg.alert("""
Ok. Have a good day!
""")
