from art import logo


def get_winner(list_of_bidders):
    greater = 0
    winner = {}
    for bidder in list_of_bidders:
        if bidder['bid'] > greater:
            greater = bidder['bid']
            winner = bidder
    print(f'The winner is {winner["name"]} with a bid of {winner["bid"]}')


print(logo)
print('Welcome to the secret auction program.')
bidders = []

while True:
    new_bidder = {'name': input('What is your name?: '), 'bid': int(input('What is your bid?: $'))}
    bidders.append(new_bidder)
    if input('Are there any other bidders? Type "yes" or "no". ').lower()[0] == 'n':
        break

get_winner(bidders)
