from datetime import *

current_date = datetime.now()
print(current_date)

current_year = current_date.year
print(current_year)

current_month = current_date.month
print(current_month)

current_day = current_date.day
print(current_day)

current_hour = current_date.hour
print(current_hour)

day_of_week = current_date.weekday()
print(day_of_week)

date_of_birth = datetime(year=1994, month=11, day=5, hour=4, minute=10)
print(date_of_birth)

