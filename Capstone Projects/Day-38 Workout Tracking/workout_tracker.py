import requests
import json
from datetime import datetime
##---------------------------------------NUTRITIONX---------------------------------##
# URL for the Nutritionix API endpoint
nutri_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutri_headers = {
    'Content-Type': 'application/json',
    'x-app-id': "NUTRINIX_APP_ID",
    'x-app-key': "NUTRINIX_API_KEY"
}
nutri_body = {
    "query": input("What Workouts You have Done Today ? ")
}

nutri_response = requests.post(url=nutri_url, headers=nutri_headers, data=json.dumps(nutri_body))
# print(nutri_response.json())
Exercises = nutri_response.json()["exercises"]
##---------------------------------------SHEETY---------------------------------##
# URL for the Sheety API endpoint
sheet_url = 'https://api.sheety.co/SHEETY_API/workoutTracking/workouts'
for exercise in Exercises:
    today = datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")
    # Data to be posted
    sheet_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration(min)": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    # print(sheet_body)
    headers = {
            'Content-Type': 'application/json'
    }

    # Make the POST request
    sheet_response = requests.post(url=sheet_url, headers=headers, data=json.dumps(sheet_body))
    # Check the response
    if sheet_response.status_code == 200:
        print('Row added successfully')
        print(sheet_response.json())
    else:
        print('Failed to add row')
        print(sheet_response.text)
