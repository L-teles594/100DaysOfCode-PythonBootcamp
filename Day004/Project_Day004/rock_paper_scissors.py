"""
Instructions
Make a rock, paper, scissors game.

Inside the blackjack.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors Association website.


"""
from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [rock, paper, scissors]
player_choice = int(input('What is your choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. '))
computer_choice = randint(0, 2)

if player_choice in range(0, 3):
    print(choices[player_choice])
    print("Computer chose\n", choices[computer_choice])

if player_choice == computer_choice:
    print('Draw')
elif player_choice == 0 and computer_choice == 1:
    print("you lose")
elif player_choice == 0 and computer_choice == 2:
    print('You win')
elif player_choice == 1 and computer_choice == 0:
    print("you win")
elif player_choice == 1 and computer_choice == 2:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You lose")
elif player_choice == 2 and computer_choice == 1:
    print("You lose")
else:
    print("You aren't playing scissor, paper, rock, lizard, spock!!!")