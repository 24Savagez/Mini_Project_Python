import smtplib
from datetime import datetime
import random
import pandas as pd

# set email
MY_EMAIL = 'chutayu.adhi@yahoo.com'
MY_PASSWORD = "yiotilysazwcuhll"

# check datetime on today
today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('birthdays.csv')

# Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    # Who birthday
    birthdays_person = birthdays_dict[today_tuple]
    # Random platform
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'

    # read file and replace Name's birthday
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthdays_person['name'])

    # send email
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person['email'],
            msg=f"Subject:Happy Birthday\n\n {contents}"
        )
