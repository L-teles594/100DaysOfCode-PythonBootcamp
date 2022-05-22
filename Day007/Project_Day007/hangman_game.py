# Step 5

from random import choice
import ascii_art as a
import list_of_words as l
import os

clear = lambda: os.system('cls')
chosen_word = choice(l.word_list)
lives = 6

print(a.logo)

# Create blanks
display = ['_' for letter in chosen_word]
guessed_letters = []

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in guessed_letters:
        guessed_letters += guess
    else:
        print(f"You've already guessed the {guess} letter")
    # Check guessed letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'The {guess} letter is not in the word!')
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(a.stages[lives])
    print(f"{' '.join(display)}")

# Check if user has got all letters.
if '_' not in display:
    print('You Win!')
elif lives == 0:
    print('You Lose!')
