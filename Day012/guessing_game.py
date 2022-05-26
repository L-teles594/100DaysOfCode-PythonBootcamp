def difficulty():
    while True:
        msg = input("Choose dificulty. Type 'easy' or 'hard'. ").lower()[0]
        if msg == 'e':
            return 10
        elif msg == 'h':
            return 5
        else:
            print('Choose a valid dificulty')


def comparing_numbers(secret_n, player_guess):
    if secret_n == player_guess:
        print(f'You got it! The answer is {secret_n}')
        return True
    else:
        if player_guess > secret_n:
            print('Too high.')
        else:
            print('Too low.')
        return False


def can_continue(live_to_check):
    if live_to_check == 0:
        print('You lose!')
        return False
    else:
        print(f'You have {live_to_check} attempts remaining to guess the number')
        return True


def main():
    from art import logo
    from random import randint

    # Messages from the game
    print(logo)
    print('Welcome to the number Guessing Game!')
    print("I'm Thinking of a number between 1 and 100.")

    # Setting variables up
    lives = difficulty()
    secret_number = randint(1, 100)
    print(secret_number)

    while True:
        # Making the guess and checking it
        guess = int(input('Make a guess: '))
        if comparing_numbers(secret_number, guess):
            return
        else:
            lives -= 1
            if not can_continue(lives):
                break


main()
