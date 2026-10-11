import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("RailRadarAPI")

class IRCTC:

    def __init__(self):
        user_input=input("""How would you like to proceed?
            1. Enter 1 to check live train status
            2. Enter 2 to check PNR
            3. Enter 3 to check train schedule""")

        if user_input == '1':
            print('Live train status')
        elif user_input == '2':
            print('PNR')
        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("Enter the train no: ")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        response = requests.get(
            "https://api.railradar.in/v1/trains/12919?haltsOnly=true",
            headers={"Authorization": api_key},
            params={'train_no':train_no}
        )
        response.raise_for_status()
        result = response.json()

        if not result.get('success'):
            print("API request failed:", result)
            return
        data = result.get('data',{})
        route = data.get("route")

        if route is None:
            print("Train route unavailable. API response",result)
            return

        for station in route:
            print(station)

obj = IRCTC()
