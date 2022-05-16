"""
Instructions
Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g.
    any value of a and b.

Example Input
a: 3
b: 5
Example Output
a: 5
b: 3
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/tgdNl0iSqK6RpPyYZh9d

Hint
You should not have to type any numbers in your code.
You might need to make some more variables.
"""

a = int(input('Enter a integer number: '))
b = int(input('Enter another integer number: '))

c = a
a = b
b = c
print(a,b)