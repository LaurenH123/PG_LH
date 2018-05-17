import pyautogui as pg
import time


points = 0


# Question 1

answer = pg.prompt (
    
"""

Which would you rather do?

a)Read, Read, Read?
b)Play a sport of your choice?
c)Make some crafts of your choice?
d)Watch netflix or youtube?
"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4


# Question 2

answer = pg.prompt (
"""

Which would you rather do for break?

a)Have a staycation?
b)Go skiing somewhere cold such as Utah, Coloado or Vermont? 
c)Go internationaly to explore a new country or a country you love?
d)Go somewhere warm such as Bahamas, Florida, or Saint Barths? 

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

 # Question 3

answer = pg.prompt (
"""

Where would you rather go for food?

a)McDonalds
b)Subway
c)Starbucks
d)Green and Tonic

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4



# Question 4

answer = pg.prompt (
"""

Which would you rather have for desert?

a)Ice cream all the way
b)Apple pie
c)Cake
d)Cookie/Brownies

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

 # Question 5

answer = pg.prompt (
"""

Which would you rather watch?

a)I am not a TV person
b)How I met your mother?
c)90210?
d)Gosip Girl?

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

 # Question 6

answer = pg.prompt (
"""

Where would you rather go to get clothes?

a)Idk where ever there is clothing
b)Addidas? 
c)Urban Outfiters?
d)Brandy Melvil all the way?

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

 # Question 7

answer = pg.prompt (
"""

What is your part of the school day?

a)Academics
b)Sports
c)Arts
d)Seeing friends 

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

# Question 8

answer = pg.prompt (
"""

What after school activity do you like the most?

a)Mathletes
b)ALL SPORTS
c)All Arts
d)Dance

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4


# Question 9

answer = pg.prompt (
"""

What do you like to listen to?

a)The Beatles
b)My workout playlist
c)Pop music
d)Chance the rapper

"""
    )

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

 # Question 10

answer = pg.prompt (
"""

What your favorite type of Genre?

a)Non Fiction
b)Sports books
c)Poetry
d)Realistic Fiction


"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

# Question 11

answer = pg.prompt (
"""

What is your season?

a)Fall?
b)Spring? 
c)Winter?
d)Summer?

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

# Question 12

answer = pg.prompt (
"""

What is your favorite tree?

a)Mapple?
b)Pine? 
c)Birch?
d)Oak?

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4
 
# Question 13

answer = pg.prompt (
"""

What is your favorite Movie?

a)Documenteries
b)Kicking and Screaming
c)Pitch Perfect 
d)Mean Girls

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4

# Question 14

answer = pg.prompt (
"""

What is your favorite type of Pasta?

a)Spagettie?
b)Wheles? 
c)Bow Tie?
d)Penne?

"""
    )

# Give points

if answer == "a":
    ponts += 1
elif answer == "b":
    points += 2
elif answer == "c":
 points += 3
elif answer == "d":
 points += 4



# END OF SURVEY

pg.alert ("You are...")

#Nerdy
if points < 21:
    pg.alert ("Option 1")

#Sporty
elif points >= 21 and points < 35:
    pg.alert("Option 2")

#Artsy
elif points >= 35 and points < 49:
    pg.alert("Option 3")

#Girly Girl
elif points >= 49 and points <= 56:
    pg.alert("Option 3")

    
