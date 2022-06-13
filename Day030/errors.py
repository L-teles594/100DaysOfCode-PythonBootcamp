"""
Issue
We've got some buggy code. Try running the code. The code will crash and give you an IndexError. This is because we're
looking through the list of fruits for an index that is out of range.

Bad Output
https://cdn.fs.teachablecdn.com/GNPYLwHXQFOUTylnvWvK
"""
fruits = ["Apple", "Pear", "Orange"]



def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")


make_pie(2)
make_pie(4)
make_pie(0)
make_pie(3)



