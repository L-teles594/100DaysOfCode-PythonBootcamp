with open('./PycharmProjects/100DaysOfCode-PythonBootcamp/Day026/file1.txt') as data:
    data1 = map(int, data.read().split('\n'))
    print(data1)

with open('file2.txt') as data:
    data2 = map(int, data.read().split('\n'))
    print(data2)

result = [n for n in data1 if n in data2]
# Write your code above 👆

print(result)
