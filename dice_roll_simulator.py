"""The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the random module in the Python programming language.
we’ll use the random.randint() function. This function returns a random integer based on the start and end we specify.
The smallest value of a dice roll is 1 and the largest is 6, this logic can be used to simulate a dice roll. This gives us the start and end values to use in our random.randint() function. """



# importing module for random number generation
import random

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices....")
    print("The values are :")

    #generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val,max_val))

    #generating and printing 2nd ransom integer from 1 to 6
    print(random.randint(min_val,max_val))

    #asing the user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?")