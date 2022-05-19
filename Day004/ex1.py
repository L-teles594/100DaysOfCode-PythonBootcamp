from random import randint

your_choice = input("What do you want? 'heads' or 'tails' ").lower()
toss_coin = randint(0, 1)
if toss_coin == 0:
    print("""
     _                    _ 
    | |                  | |
    | |__   ___  __ _  __| |
    | '_ \ / _ \/ _` |/ _` |
    | | | |  __/ (_| | (_| |
    |_| |_|\___|\__,_|\__,_|
    """)
else:
    print("""
 _          _ 
| |      ( ) |
| |_ __ _ _| |
| __/ _` | | |
| || (_| | | |
 \__\__,_|_|_|
    """)
if your_choice == 'heads' and toss_coin == 0:
    print('You win!')
elif your_choice == 'tails' and toss_coin == 1:
    print('You win!')
else:
    print("You lose!")