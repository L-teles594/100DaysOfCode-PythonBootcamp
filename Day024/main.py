file = open('my_file.txt', )
content = file.read()
print(content)
file.close()

with open('my_file.txt', mode='w') as file:
    file.write('\nThat is a new line on the document!')

with open('new_file.txt', mode='a') as file:
    file.write('Here is a new document.\nCreated with python!')


