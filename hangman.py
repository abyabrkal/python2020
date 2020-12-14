# ANGELA - 100 DAYS OF PY
# HANGMAN

import random

word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)


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
  
  print(display)

  if '_' in display:
    end_of_game = True
    print('You win.')
