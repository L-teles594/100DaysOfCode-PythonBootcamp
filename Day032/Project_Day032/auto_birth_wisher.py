from pandas import read_csv
from smtplib import *
from random import randint
from datetime import *


def letter_generator(name):
    file_str = f'letter_{randint(1, 3)}.txt'

    with open(f'letter_templates/{file_str}') as file:
        letter_frame = file.read().replace('[NAME]', name)

    return letter_frame
# Extra Hard Starting Project #


# 1. Update the birthdays.csv
data = read_csv('birthdays.csv')
data = data.to_dict(orient='records')
my_email = 'appbreweryinfo@gmail.com'
password = 'abcd1234()'

# 2. Check if today matches a birthday in the birthdays.csv
current_date = datetime.now()
current_month_and_day = {'month': current_date.month, 'day': current_date.day}
print(current_month_and_day)

for line in data:
    if line['month'] == current_month_and_day['month'] and line['day'] == current_month_and_day['day']:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter = letter_generator(line['name'])
        # 4. Send the letter generated in step 3 to that person's email address.
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=line['email'], msg=f'Subject:Happy Birthday\n\n{letter}')

