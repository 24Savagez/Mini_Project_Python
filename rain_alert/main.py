import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "15287b3801bf502176b265c647b3b2a8"

parameters = {
    "lat": 14.039736,
    "lon": 100.613427,
    # "exclude": "hourly",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
print(response.status_code)
data = response.json()

print(data)
