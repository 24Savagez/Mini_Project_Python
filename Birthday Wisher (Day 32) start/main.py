# import smtplib
#
# my_email = "chutayu.adhi@yahoo.com"
# my_password = "mjywgsghbgptzayo"
#
# with smtplib.SMTP("smtp.mail.yahoo.com", 587, timeout=120) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="chutayu.adhi@gmail.com",
#         msg="Subject:Hello\n\nGG WP Bro Dota2."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day)
#
# date_of_birth = dt.datetime(year=1989, month=4, day=2, hour=2, minute=45)
# print(date_of_birth)

import datetime as dt
import random
import smtplib

my_email = "chutayu.adhi@gmail.com"
my_password = "Kiss7468"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="chutayu.adhi@yahoo.com",
        msg=f"Subject:Hello Thursday\n\n{quote}"
    )
