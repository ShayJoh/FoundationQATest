#imports the Random library
import random

# Determine dice roll
def dicesides (num_sides):
    # enter the number of sides for your dice to roll one once
    return random.randint(1,num_sides)
 
# Roll as many times as specified
def roll (num_dice, num_sides):
    return [dicesides(num_sides) for i in range(num_dice)]
    #templist = []
    #for i in range(num_dice):
    #    templist.append(dicesides(num_sides))
    #return(templist)


def dice_bot():
    num_dice = num_sides = 0
    # While Loop to validate input as an integer
    while True:
        try:
            player_name = str(input("What is your name?:\n"))
            num_dice = int(input("How many dice?: "))
            num_sides = int(input("How many sides to the dice?: "))
            dc_set = 0.75 * (num_dice * num_sides)
        except ValueError:
            print("That is not a number ¯\_(ツ)_/¯")
            continue
        else:
            break


    # Determine results
    result = roll(num_dice, num_sides)
    totalresult = sum(result)

    def difficulty():
        if totalresult >= dc_set:
            return str("Yes!")
        else:
            return str("No!")

  
    print(f"\nName: {player_name}")
    print(f"Rolls: {result}")
    print(f"Total: {totalresult}")
    print(f"Do you succeed?: {difficulty()} (DC: {dc_set})\n")

dice_bot()