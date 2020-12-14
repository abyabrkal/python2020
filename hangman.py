# ANGELA - 100 DAYS OF PY
# HANGMAN

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
lives = 6

display = ['_' for _ in chosen_word]
print(display)

end_of_game = False
while not end_of_game:
  guess = input("Enter a letter: ").lower()

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print(f"Correct word: {chosen_word}. You lose.")

  print(f"{' '.join(display)}")

  if '_' not in display:
    end_of_game = True
    print('You win.')

  print(stages[lives])
