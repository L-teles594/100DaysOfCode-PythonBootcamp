def get_cards(hand):
    from random import choice
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    get_hand = []
    for _ in range(hand):
        get_hand.append(choice(cards))
    return get_hand


def check_hands(p1, p2):
    if 11 in p1:
        ask = int(input('You have an Ace, do you want 1 or 11?: '))
        if ask == 1:
            p1.remove(11)
            p1.append(1)
    if sum(p2) < 17:
        p2 += get_cards(1)

    score_p1 = sum(p1)
    score_p2 = sum(p2)
    return score_p1, score_p2


def get_winner(p1, p2):
    if p1 > 21:
        return 'You Lose'
    elif p1 == p2:
        return 'Draw'
    elif p1 > p2:
        return 'You Won'
    else:
        return 'You Lose'


def blackjack():
    from Day011.Project_Day011.art import logo
    print(logo)

    # Dealing player and computer hands
    player_hand = get_cards(2)
    player_score = sum(player_hand)
    computer = get_cards(2)
    print(f'Your cards: {player_hand}, current score: {player_score}')
    print(f"Computer's first card {computer[0]}")

    # Dealing more cards to the player
    while True:
        get_more = input("Type 'y' to get another card, type 'n' to pass: ").lower()[0]
        if get_more == 'y':
            player_hand += get_cards(1)
            player_score = sum(player_hand)
            print(player_hand, player_score)
        else:
            break

    # Checking both players hands
    player_score, computer_score = check_hands(player_hand, computer)

    # Checking the match winner
    print(get_winner(player_score, computer_score), player_hand, computer)


while True:
    do_continue = input('Do you want to play a game of Blackjack? Type "y" or "n" ').lower()[0]
    if do_continue == 'y':
        blackjack()
    else:
        break
