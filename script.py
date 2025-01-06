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
    
def save_to_csv(data, filename, columns, look_for_duplicates=True):
    try:
        if look_for_duplicates and os.path.exists(filename):
            print(f"File '{filename}' already exists. Skipping save.")
            return
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Intestazioni
            writer.writerows(data)   # Dati
        print(f"Data saved to {filename}.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
    
def main(start_date="2024-12-21"):
    client = authenticate()
    if not client:
        return
    
    end_date = datetime.now().strftime("%Y-%m-%d")

    date_list = [
        (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=i)).strftime("%Y-%m-%d")
        for i in range((datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1)
    ]

    heart_rate_data = {}
    for date in date_list:
        print(f"Fetching heart rate data for {date}...")
        daily_data = fetch_heart_rate(client, date)
        if daily_data:
            heart_rate_data[date] = daily_data
            save_to_csv(
                daily_data,
                f"data/raw/heart_rates/{date}.csv",
                ["timestamp", "heart_rate"],
                look_for_duplicates=True
            )
        
    print("Data collection complete.")


if __name__ == "__main__":
    main()