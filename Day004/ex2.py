# The Banker Roulette - Who will pay the bill?
from random import choice

group = input('Give me everybody\'s names, separated by a comma. ').split(', ')

choosen = choice(group)
print(f"The payer will be {choosen}")
