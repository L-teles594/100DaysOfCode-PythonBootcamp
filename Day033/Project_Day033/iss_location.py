import requests
from datetime import datetime
from smtplib import *
from time import sleep

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

print(sunrise, sunset, time_now)
condition1 = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
condition2 = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
condition3 = time_now not in range(sunrise, sunset + 1)

print(condition1, condition2, condition3)

while True:
    sleep(60)
    if condition1 and condition2 and condition3:
        print('look up!')
        my_email = 'appbreweryinfo@gmail.com'
        password = 'abcd1234()'
        msg = 'Subject: ISS Location\n\nLook up to see ISS at your current location!'
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='appbrewery@yahoo.com', msg=msg)
