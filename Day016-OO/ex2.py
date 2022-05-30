from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Bulbassauru', 'Charmander'] )
table.add_column('Pokemon Type', ['Electric', 'Water', 'Plant', 'Fire'])
table.align = 'l'
print(table)
