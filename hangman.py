# 100 DAYS OF PY
# HANGMAN

import random
from hangman_data import word_list, stages, logo
import os

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
lives = 6
clear = lambda: os.system('clear')

print(logo)
display = ['_' for _ in chosen_word]

end_of_game = False
while not end_of_game:
  guess = input("Enter a letter: ").lower()

  clear()

  if guess in display:
    print(f"You have already guessed this letter {guess}.")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed a letter not in the word. You LOSE 1 LIFE.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"Correct word: < {chosen_word} >. You LOSE.")

  print(f"{' '.join(display)}")

  if '_' not in display:
    end_of_game = True
    print('You WIN.')

  print(stages[lives])
