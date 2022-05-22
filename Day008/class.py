# Review:
# Create a function called greet().
def greet():
    print('Hello World!')
    print('This is my new function!')
    print("I'm realy happy!")
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
greet()


def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}')


greet_with_name('Billy')

# functions with more than 1 input


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'How is it like in {location}')


greet_with('Jack', 'London')
greet_with(location='Moscow', name='Dimitri')




