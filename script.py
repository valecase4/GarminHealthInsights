import os
from garminconnect import Garmin
from dotenv import load_dotenv
import csv
from datetime import datetime, timedelta

load_dotenv()
EMAIL = os.getenv("GARMIN_EMAIL")
PASSWORD = os.getenv("GARMIN_PASSWORD")

def authenticate():
    try:
        client = Garmin(EMAIL, PASSWORD)
        client.login()
        print("Authentication successful!")
        return client
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None
    
def fetch_heart_rate(client, date):
    try:
        data = client.get_heart_rates(date)['heartRateValues']
        converted_data = [
            [datetime.fromtimestamp(item[0] / 1000).strftime("%H:%M"), item[1]]
            for item in data
        ]
        print(f"Heart rate data retrieved for {date}.")
        return converted_data
    except Exception as e:
        print(f"Error fetching heart rate data: {e}")
        return None
    
def main():
    client = authenticate()
    if not client:
        return
    
    date = datetime.now().strftime("%Y-%m-%d")

    heart_rate_data = fetch_heart_rate(client, date)
    if heart_rate_data:
        print(heart_rate_data)

if __name__ == "__main__":
    main()