'''
Create a dice roller.

Scope: User is able to input XdY, the results are displayed and summed.
X = Number of Dice
Y = Sides available on Dice (ie, upper limit)

Ensure code is fully notated
'''
#imports the Random library
import random

# While Loop to validate input as an integer
while True:
    try:
        uinputX = int(input("How many dice?: "))
        uinputY = int(input("How many sides to the dice?: "))
    except ValueError:
        print("That is not a number ¯\_(ツ)_/¯")
        continue
    else:
        break

# Determine dice roll
def dicesides ():
    return random.randint(1,uinputY)
 
# Roll as many times as specified
def roll (uinputX):
    templist = []
    for i in range(uinputX):
        templist.append(dicesides())
    return(templist)

# Determine results
result = roll(uinputX)
totalresult = sum(result)

# Display the results
print("Rolls: ", result)
print("Total: ", totalresult)