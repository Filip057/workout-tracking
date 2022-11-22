import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "95bd1451"

API_KEY = "a4ce452eae3c0858e7cd5908311119a0"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

body = {
    "query": input("What have you done?"),
    "gender": "male",
    "weight_kg": 101,
    "height_cm": 187.5,
    "age": 26
}

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api = "https://api.sheety.co/746a7934f90fbcc6dc5837603e09f011/workout/workouts"

today = datetime.today()

response = requests.post(url=nutritionix_url, headers=headers, json=body)

workout_data = response.json()["exercises"]

for work in workout_data:
    exercise = work["name"]
    calories = work["nf_calories"]
    duration = work["duration_min"]
    date = datetime.strftime(today, "%Y/%m/%d")
    time = datetime.strftime(today, "%H:%M")

    exercise_log = {"workout":
        {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    user = "filipp"
    passw = "asjdlkjh1"

    basic = HTTPBasicAuth(user, passw)

    sheet_response = requests.post(url=sheety_api, json=exercise_log, auth=basic)
