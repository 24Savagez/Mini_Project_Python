import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = 65
HEIGHT_CM = 166
AGE = 32

APP_ID = "9ed36947"
API_KEY = "895390fcec11fbb616b05a22e93fb3b6"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/540bbaacd729d8738567c7fc69c08bea/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

#
today_date = datetime.now().strftime('%d/%m/%Y')
time_now = datetime.now().strftime('%X')

sheet_headers = {
    "Content-Type": "application/json"
}

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            "date": today_date,
            'time': time_now,
            'exercise': exercise['user_input'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    # 1.NO Authentication
    # sheet_response = requests.post(sheet_endpoint, json=sheet_input, headers=sheet_headers)
    # print(sheet_response.text)

    # 2.Basic Authentication
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_input,
    #     headers=sheet_headers,
    #     auth=(
    #         "Chutayu",
    #         "Kiss7468"
    #     )
    # )
    # print(sheet_response.text)

    # 3.Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer @Kiss7468"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_input,
        headers=bearer_headers
    )
    print(sheet_response.text)


