import random

number = random.randint(0,3)

words = ["BUBBLE", "HOW I MET YOUR MOTHER", "ICE CREAM", "DOG"]
hint1 = ["------ bath", "Ted", "dessert", "animal" ]
hint2 = ["soap", "Robin", "cold", "hate cats" ]

secretword = words[number]
guess = ""
counter = 1

while True:
    print ("Guess the secret word!")
    print ("Type 'hint1', 'hint2' 'first letter' or 'give up' for answer.")
    guess = input(). upper()

    if guess == secretword:
        print("You won!")
        print("It took you " + str (counter) + " guess.")
        break
    
    elif guess == "HINT1":
        print( hint1[number] )
        
    elif guess == "HINT2":
        print( hint2[number] )
        
    elif guess == "FIRST LETTER":
        print( secretword[0] )

    elif guess == "GIVE UP":
        print("The secret word was " + secretword)
        print(" You failed" + str(counter) + "times.")
        break

    else:
        counter += 1
        print("Guess again")
