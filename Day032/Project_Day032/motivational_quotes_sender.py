from datetime import *
from smtplib import *
from random import choice

with open('quotes.txt') as file:
    quotes = file.read().split('\n')

quote = choice(quotes)
message = f'Subject:Monday Motivation\n\n{quote}'

current_date = datetime.now()
is_monday = True if current_date.weekday() == 6 else False

if is_monday:
    my_email = 'appbreweryinfo@gmail.com'
    password = 'abcd1234()'
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='appbrewerytesting@yahoo.com', msg=message)
