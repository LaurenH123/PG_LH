import webbrowser as wb

name = input ("What's your name? ")
print(" Hello " + name)

food = input ("What's your favorite food")
print (name + " likes to eat" + food)

color = input ("What's your favorite color")
print (name + " likes the color" + color)

sport = input ("What's your favorite sport?")
print (name + " likes" + sport)

TV = input ("What's your favorite TV show")
print (name + " watches" + TV)

game = input ("What's your favorite game")

if game == " Fortnite":
    print ("Look, a Llama!")
    wb.open("https://www.youtube.com/watch?v=2m_1oPkhlLg")

elif game == " Monopoly":
    print("What a classic")

elif game == " Go Fish":
    print ("You already lost")

else:
    print (name + " likes to play " + game)
    
movie = input ("What's your favorite movie")

if movie == " Hunger Games":
    print (" lol you dead")

elif movie == " Divergent":
    print (" Noice")

else:
    print ("That is a great one")


