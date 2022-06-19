from smtplib import *

my_email = 'appbrewery@gmail.com'
password = 'abcd1234()'
message = 'Subject:Hello\n\nThis is the body of my email.'
with SMTP('smtp.gmail.com') as  connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='appbrewerytesting@yahoo.com', msg=message)
