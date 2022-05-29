def get_player(list_used):
    from data import data
    from random import choice
    while True:
        character = choice(data)
        if data.index(character) not in list_used:
            list_used.append(data.index(character))
            return character


def comparing(a, b, guess):
    greater = max(a["follower_count"], b["follower_count"])
    if greater == a["follower_count"] and guess == 'a':
        return True
    elif greater == b["follower_count"] and guess == 'b':
        return True
    else:
        return False


def main():
    from art import logo, vs
    print(logo)
    already_useded = []
    score = 0
    a = get_player(already_useded)
    while True:
        b = get_player(already_useded)

        print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}')
        print(vs)
        print(f'Against B: {b["name"]}, {b["description"]}, from {b["country"]}')

        guess = input("Who has more followers? 'A' or 'B': ").lower()[0]
        
        if comparing(a, b, guess):
            a = b
            score += 1
            print(logo)
            print(f"You're right! Current score {score}.")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            break


main()
