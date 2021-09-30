import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = 'chutayu.adhi@yahoo.com'
PASSWORD = 'yiotilysazwcuhll'

if weekday == 3:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=PASSWORD,
    )

    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs='chutayu.adhi@bumail.net',
        # to_addrs='watcharich.pala@bumail.net',
        msg=f'Subject:Hello\n\n {quote}'
    )
    # connection.close()
