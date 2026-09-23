import datetime
import random
import smtplib
import os

sender = "aminimohammadreza13@gmail.com"
receiver = "aminimamareza@gmail.com"

calendar = datetime.datetime.now()
today = calendar.weekday()

with open("./quotes.txt") as file:
    quotes = file.readlines()

monday_quote = random.choice(quotes)

if today == 0:
    message = f"Subject:Monday Motivation\n\n {monday_quote}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender, os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            msg=message,
            from_addr=sender,
            to_addrs=receiver
        )
