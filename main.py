import datetime
import random
import smtplib

sender = "aminimohammadreza13@gmail.com"
receiver = "aminimamareza@gmail.com"

# Monday=0 till saturday 6
calendar = datetime.datetime.now()
today = calendar.weekday()

# TODO 2: Read txt and get a random quote
with open("./quotes.txt") as file:
    quotes = file.readlines()

monday_quote = random.choice(quotes)

# TODO 3: check if it's Monday if yes send monday_quote to your email
if today == 0:
    message = f"Subject:Monday Motivation\n\n {monday_quote}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender, "znmouxwvowqhtrue")
        connection.sendmail(msg=message, from_addr=sender, to_addrs=receiver)
