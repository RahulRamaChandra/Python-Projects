"""In Python the Colorama module allows us to easily create colored terminal text.

What is Colorama in Python?

Using the Colorama module we can print colored text with Python. We can use it and call its built-in variables which are aliases for the desired ANSI codes.
This makes our code more readable and works better with Windows command prompts after calling colorama.init() at the start of your script.

The Colorama module offers three main formatting options: Fore, Back, and Style. These allow us to change the foreground or background text color and style.
The colors available for the foreground and background are black, red, green, yellow, blue, magenta, cyan, and white."""


import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is Rahul Rama Chandran "+ Fore.YELLOW+ Back.BLUE+"I'm your Machine Learning Instructor")
print(Back.CYAN+"Hi My Name is Rahul Rama Chandran")
print(Fore.RED + Back.GREEN +"Hi My name is Rahul Rama Chandran")

"""It is also possible to change other text properties using ANSI escape characters, for example, if we wanted to make the text darker or lighter.
Reference: https://pypi.org/project/colorama/"""