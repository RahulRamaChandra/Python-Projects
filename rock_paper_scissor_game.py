"""To create the Rock, Paper and Scissors game with Python,
we need to take the user’s choice and then we need to compare it with the computer choice which is taken using the random module in Python from a list of choices,
and if the user wins then the score will increase by 1:
"""


import random
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    computer = random.choice(choices)
    print(computer)
    
    ## Conditions for Rock,Paper and scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        else: 
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player , "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
            player_score += 1
    elif player == "End":
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
