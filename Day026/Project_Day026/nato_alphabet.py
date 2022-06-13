from pandas import read_csv

data = read_csv('nato_phonetic_alphabet.csv')

code = {row.letter: row.code for ind, row in data.iterrows()}

while True:
    try:
        coded = [code[letter] for letter in input('Enter a word: ').upper()]
    except KeyError:
        print('Sorry, only letters in alphabet please.')
    else:
        print(coded)
        break

