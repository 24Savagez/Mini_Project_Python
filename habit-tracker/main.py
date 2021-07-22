import requests
from datetime import datetime

USERNAME = "savage"
TOKEN = "yRjuy5&Z5d9Ui&J"
ID_GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": ID_GRAPH,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post value on graph
# today = datetime(year=2021, month=7, day=21)
today = datetime.now()

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}"
body_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? : "),
}

response = requests.post(url=graph_endpoint, json=body_config, headers=headers)
print(response.text)

# # Change value
# date_update = datetime.now().strftime("%Y%m%d")
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}/{date_update}"
# update_data = {
#     "quantity": "10.23"
# }

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# Delete value
# delete_vale = datetime.now().strftime("%Y%m%d")
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}/{delete_vale}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
