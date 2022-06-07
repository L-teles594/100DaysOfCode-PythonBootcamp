with open('Input/Names/invited_names.txt', mode='r') as data:
    names = list(data.read().split('\n'))
print(names)

with open('Input/Letters/starting_letter.txt', mode='r') as data:
    letter = data.read()
print(letter)

for name in names:
    final_letter = letter.replace('[name]', name)
    print(final_letter)
    with open(f'Output/ReadyToSend/{name}_invitation_letter.txt', mode='a') as data:
        data.write(final_letter)
