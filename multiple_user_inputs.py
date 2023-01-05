"""
The input() function of Python help us to give a user input while writing a program.

Problem Statement for Taking Multiple User Inputs with Python:

Suppose you are prompted to write a Python program that interacts with a user in a console window. 
You may be accepting input to send to a database, or reading numbers to use in a calculation.
Whatever the purpose, you should code a loop that reads one or multiple user inputs from a user typing on a keyboard and prints a result for each.
In other words, you have to write a classic print loop program.
"""

# Multiple Inputs with Python using While Loop

while True:
    reply = input("Enter Text: ")
    if reply == 'stop': break
    print(reply)