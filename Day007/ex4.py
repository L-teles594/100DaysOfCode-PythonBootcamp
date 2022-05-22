# Step 4

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

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_' for letter in chosen_word]

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1

    # Join all the elements in the list and turn it into a String.

    print(stages[lives])
    print(f"{' '.join(display)}")

    # Check if user has got all letters.

if "_" not in display:
    print("You win.")
else:
    print("You lose")
