import smtplib
import random
import datetime as dt
import os
import pandas as pd

PATH = os.path.dirname(__file__)

today = dt.datetime.now()
##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

def send_email(msg,mail):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("user"), password=os.getenv("pass"))
        connection.sendmail(from_addr=os.getenv('user'), to_addrs=mail, msg=f"Subject:Happy Birthday\n\n{msg}")


birthdays = pd.read_csv(os.path.join(PATH, 'birthdays.csv'))

for bday in birthdays.iterrows():
    if bday[1]['month'] == today.month and bday[1]['day'] == today.day:
        with open(os.path.join(PATH, f"letter_templates/letter_{random.randint(1,3)}.txt")) as file:
            file = file.read()
            file = file.replace("[NAME]", bday[1]['name'])
            send_email(file, bday[1]['email'])






