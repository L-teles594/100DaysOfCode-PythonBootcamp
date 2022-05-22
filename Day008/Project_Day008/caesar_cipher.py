from art import logo


def caesar(plain_text, shift_amount, cipher_direction):
    caesar_cipher = ''
    global alphabet
    for letter in plain_text:
        if letter not in alphabet:
            caesar_cipher += letter
            continue
        if cipher_direction == 'encode':
            index_of_encoded = alphabet.index(letter) + shift_amount
            if index_of_encoded <= 25:
                caesar_cipher += alphabet[index_of_encoded]
            else:
                caesar_cipher += alphabet[index_of_encoded - 26]
        elif cipher_direction == 'decode':
            index_of_decoded = alphabet.index(letter) - shift_amount
            caesar_cipher += alphabet[index_of_decoded]
    print(f'The {cipher_direction}d text is {caesar_cipher}')


while True:
    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != 'encode' and direction != 'decode':
        print("Invalid option, let's try again")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    if input('Do you want to play again? "yes" or "no" ').lower()[0] == 'n':
        break

"""
When the letter to be shifted gone out of range just made a condition to subtract 26 of the index, for encode
and add to decode
 For decoding a message in python we don't have to adjust the index because python accepts negative indexes,
 else we would have to use this:
 index_of_encoded = alphabet.index(letter) - shift_amount
        if index_of_encoded <= 25:
            caesar_cipher += alphabet[index_of_encoded]
        else:
            caesar_cipher += alphabet[index_of_encoded + 26]
"""
