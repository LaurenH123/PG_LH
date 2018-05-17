import webbrowser
name = "Lauren"

subjects = ["English", "Math", "Science", "History", "Chinese"]

print ("Hello " + name)

print(subjects)

for i in subjects:
    print("One of my classes is " + i)

icecream =["Caramel", "Cotton Candy", "Cake Batter", "Vanilla", "Chocolate"]

for i in icecream:
    if i == "caramel":
         print(i + " is the best.")
    elif i == "cake batter":
         print(i + " is the seccond best.")
    elif i == "cotton candy":
         print(i + " is the third best.")
    elif i == "vanila":
         print(i + " is the most basic but is the fourth best.")
    elif i == "Chocolate":
         print(i + " is the worst flavor ever.")

tvshows = []

while True:
    print("What is a tvshow you like? Type 'end' to quit")
    answer = input()
    if answer == "end":
        break

    else:
        tvshows.append(answer)

for i in tvshows:
    print("One of your favorite is " + i)
    webbrowser.open(i)

        
