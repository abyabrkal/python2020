
# Online Python - IDE, Editor, Compiler, Interpreter
# Number Guessing Game
import random

logo = """
   ______                        _   __              
  / ____/_  _____  __________   / | / /_  ______ ___ 
 / / __/ / / / _ \/ ___/ ___/  /  |/ / / / / __ `__ \
/ /_/ / /_/ /  __(__  |__  )   / /|  / /_/ / / / / / /
\____/\__,_/\___/____/____/  /_/ |_/\__,_/_/ /_/ /_/ 
"""
print(logo)
print("Welcome to Number Guessing Game.")

EASY_DIFFICULTY = 5
HARD_DIFFICULTY = 10

def guess_number(attempts):
    ''' Guess a number mechanics '''
    random_number =  random.randint(1,100)
    for count in range(attempts):
        print(f"You have {attempts-count} attempts remaining.")
        guess = int(input("Enter your guess"))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
        else:
            print(f"You guess it. [{random_number}]")
            return
    

continue_game = True
while continue_game:
    difficulty = input("Do you play hard(h) or easy(e)").lower()
    if difficulty == 'h':
        print("You choose HARD!. You got 5 attempts.")
        guess_number(EASY_DIFFICULTY)
    elif difficulty == 'e':
        print("You choose EASY!. You got 10 attempts.")
        guess_number(HARD_DIFFICULTY)
    else:
        print("Invalid entry")
        
    answer = input("Do you want to play again? yes or no")
    if answer == 'yes':
        continue_game = True
    else:
        continue_game = False
