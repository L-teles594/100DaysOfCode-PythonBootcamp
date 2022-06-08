# import csv
#
# with open('weather_data.csv') as data:
#     lines = csv.reader(data)
#     temperature = []
#     for row in lines:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
# print(temperature)

# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# average = data['temp'].mean()
# print(average)
# max = data['temp'].max()
# print(max)
#

# with open('weather_data.csv', 'r') as data:
#     lines = data.read().split('\n')
#
# print(lines)

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirels = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirels = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squirels, cinnamon_squirels, black_squirels)

data_dict = {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [gray_squirels, cinnamon_squirels, black_squirels]}

data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv('squirrel_count')