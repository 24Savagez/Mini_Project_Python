import requests

api_key = "15287b3801bf502176b265c647b3b2a8"

parameters = {
    "lat": 14.039736,
    "lon": 100.613427,
    "exclude": "hourly",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.raise_for_status())
data = response.json()

print(data)
