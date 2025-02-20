import os
from twilio.rest import Client
import requests
import json

lat= "LATITUDE"
lon= "LONGITUDE"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_key = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
weather_params = {
    "lat": "LATITUDE",
    "lon": "LONGITUDE",
    "appid": API_key

}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}")
response.raise_for_status()

will_run = False

for i in range(1,6):    # we also use list comprehension method [:] and then proceed next
    print(response.json()["list"][i]["dt_txt"])
    condition_code = response.json()["list"][i]["weather"][0]["id"]
    print(condition_code)
    if int(condition_code)< 700:
        print("Bring an Umbrella")
        will_run = True
        break

if will_run:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to Rain ⛈️ today, Remember to bring an Umbrella ☂️",
        from_="FROM_MOBILE_NO",
        to="TO_MOBILE_NUMBER",
    )

    print(message.body)
