import datetime as dt
import random
import smtplib
import pandas
import os

# Change the current working directory to the Script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MY_EMAIL = "SENDER_MAIL_ADDRESS"
MY_PASSWORD = "MAIL_APP_PASSWORD"

now = dt.datetime.now()
TODAY_DAY = now.day
TODAY_MONTH = now.month

with open(file="data/birthday_wishes.txt",mode="r") as file:
    letters = file.read().split('\n\n')

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    data = pandas.read_csv("data/birthdays.csv")
    birthdays_dict = data.to_dict(orient="records")
    for person in birthdays_dict:
        if person['month'] == TODAY_MONTH and person['day'] == TODAY_DAY:
            selected_letter = random.choice(letters)
            final_wish = selected_letter.replace('[Name]',person['name'])
            recipient_email = person['email']
            print(final_wish)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birtday!\n\n{final_wish}"
            )
            print()
if connection:
    try:
        connection.quit()  # Close the connection
    except smtplib.SMTPServerDisconnected:
        print("The connection was already closed.")
