import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "15287b3801bf502176b265c647b3b2a8"
account_sid = "AC796045391d4ac83f9512e3e6441dd725"
auth_token = "cbdf5c1be13095a1b566e4fbeae83d9e"

parameters = {
    "lat": 14.0400153,
    "lon": 100.6119786,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()
# weather_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][0:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+12109780151",
        to='+66985241288'
    )
    print(message.status)
