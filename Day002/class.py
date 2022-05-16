#Data Types

# Strings

print("Hello"[0]) # Subscripting

# Integers

print(123)
print(67 + 23)
print(123_456_789)

# Float

print(3.14159)

#Booleans

True
False

print(type(123_456))

print(str(123))
print(float(123))
print(bool(123))
print(int(123.0))

# Math operators
3 + 5
3 - 2
3 * 2
6 / 6
2 ** 3
5 // 2
7 % 2

# Priority ** from right to left --> * / // % From the left to right --> + - the same direction
# all maths inside parenthesis should be solved first not regarding the priority inside it.
print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))

print(f'This is a f-string {True} {123} {456.89}')