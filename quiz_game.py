"""The Quiz game asks the player questions about animals.
They have three chances to answer each question you don’t want to take the quiz too difficult.
Each correct answer will score a point. At the end of the game, the program will reveal the player’s final score."""

"""This quiz game uses a function; a block of code with a name that performs a specific task.
A function allows you to use the same code several times, without having to type everything each time.
Python has a lot of built-in functions, but it also allows you to create your functions."""

"""The program should continue to check if there are any questions to ask and if the player has exhausted all his chances.
The score is stored in a variable during the game. Once all the questions have been answered, the game ends."""


def check_guess(guess,answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer, Try again ")
            attempt = attempt + 1
        if attempt == 3:
            print("The correct answer is ", answer)

score = 0
print("Guess the Animal")
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land Animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the largest Animal? ")
check_guess(guess3, "Blue Whale")
print("Your Score is "+ str(score))
