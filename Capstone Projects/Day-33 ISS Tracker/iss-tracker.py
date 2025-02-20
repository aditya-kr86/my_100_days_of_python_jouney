import requests
from datetime import datetime
import time
import smtplib

MY_LAT = "ENTER_YOUR_LATITUDE"
MY_LONG = "ENTER_YOUR_LONGITUDE"
MY_EMAIL = "SENDER_MAIL_ADDRESS"
MY_PASSWORD = "MAIL_APP_PASSWORD"
recipient_email = "RECEPIENT_EMAIL"

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_latitude = float(iss_response.json()['iss_position']['latitude'])
iss_longitude = float(iss_response.json()['iss_position']['longitude'])


### MY location Sunrise and Sunset
parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()

# Extract and adjust sunrise time
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1]) + 30

# Adjust for overflow in minutes
if sunrise_min >= 60:
    sunrise_min -= 60
    sunrise_hour += 1

# Adjust for overflow in hours
if sunrise_hour >= 24:
    sunrise_hour -= 24

# Extract and adjust sunset time
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5
sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1]) + 30

# Adjust for overflow in minutes
if sunset_min >= 60:
    sunset_min -= 60
    sunset_hour += 1

# Adjust for overflow in hours
if sunset_hour >= 24:
    sunset_hour -= 24

def location_matcher(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
    # Check if the ISS is within 5 degrees latitude and longitude
    if abs(iss_latitude - MY_LAT) <= 5.0 and abs(iss_longitude - MY_LONG) <= 5.0:
        return True
    else:
        return False

def is_dark():
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    
    if (current_hour < sunrise_hour) or (current_hour == sunrise_hour and current_min < sunrise_min):
        return True
    elif (current_hour > sunset_hour) or (current_hour == sunset_hour and current_min >= sunset_min):
        return True
    else:
        return False

while True:
    time.sleep(60)
    if location_matcher(MY_LAT, MY_LONG, iss_latitude, iss_longitude) and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipient_email,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the Sky"
            )
        if connection:
            try:
                connection.quit()  # Close the connection
            except smtplib.SMTPServerDisconnected:
                print("The connection was already closed.")

