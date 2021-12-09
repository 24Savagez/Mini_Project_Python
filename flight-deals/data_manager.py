import requests
from pprint import pprint

API_SHEETY_ENDPOINT = "https://api.sheety.co/540bbaacd729d8738567c7fc69c08bea/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the sheety API to get all the data in that sheet and print it out.
        response = requests.get(url=API_SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']

        # 3. try importing pretty print and printing the data out again using ppprint() to see formatted.
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{API_SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)
