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

def fetch_steps(client, date):
    try:
        steps_sum = 0
        data = client.get_steps_data(date)
        for record in data:
            steps_sum += record['steps']
        print(f"Step data retrieved for {date}.")
        return steps_sum
    except Exception as e:
        print(f"Error fetching step data: {e}")
        return None

def fetch_activity_data(client):
    try:
        activities = client.get_activities(0, 1000) 
        print("Activity data retrieved.")
        return activities
    except Exception as e:
        print(f"Error fetching activity data: {e}")
        return None
    
def fetch_sleep_stages_data(client, date):
    stages = {
        0: "Deep",
        1: "Light",
        2: "REM",
        3: "Awake"
    } 

    try:
        data = client.get_sleep_data(date)['sleepLevels']
        sleep_data_stages = []
        for record in data:
            start_gmt_time = datetime.strptime(record['startGMT'], "%Y-%m-%dT%H:%M:%S.%f")
            start_local_time = (start_gmt_time + timedelta(hours=1)).strftime("%H:%M")
            end_gtm_time = datetime.strptime(record['endGMT'], "%Y-%m-%dT%H:%M:%S.%f")
            end_local_time = (end_gtm_time + timedelta(hours=1)).strftime("%H:%M")
            sleep_stage = stages[int(record['activityLevel'])]

            sleep_data_stages.append([start_local_time, end_local_time, sleep_stage])
        
        return sleep_data_stages
    
    except Exception as e:
        print(f"Error fetching sleep data (stages): {e}")
        return None

def fetch_sleep_heart_rates_data(client, date):
    try:
        data = client.get_sleep_data(date)['sleepHeartRate']
        heart_rates_sleep_data = []
        for record in data:
            heart_rate = record['value']
            timestamp = datetime.fromtimestamp(int(record['startGMT']) / 1000)
            timestamp = timestamp.strftime("%H:%M")
            heart_rates_sleep_data.append([heart_rate, timestamp])
        
        return heart_rates_sleep_data

    except Exception as e:
        print(f"Error fetching sleep data (heart rates): {e}")
        return None
    
def save_to_csv(data, filename, columns, look_for_duplicates=True):
    try:
        if look_for_duplicates and os.path.exists(filename):
            print(f"File '{filename}' already exists. Skipping save.")
            return
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns) 
            writer.writerows(data) 
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

    # HEART RATE DATA
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

    # ACTIVITIES
    activities = fetch_activity_data(client)
    days_with_activities = []
    if activities:
        for activity in activities:
            day = activity['startTimeLocal'].split(" ")[0]
            days_with_activities.append(day)

    activities_data = []
    for date in date_list:
        if not date in days_with_activities:
            activities_data.append([date, "No"])
        else:
            activities_data.append([date, "Yes"])
    
    save_to_csv(
        activities_data,
        "data/raw/activities/activities.csv",
        ["date", "activity (Y/N)"],
        look_for_duplicates=False
        )
    
    # SLEEP STAGES
    for date in date_list:
        sleep_stages_data = fetch_sleep_stages_data(client, date)
        save_to_csv(
            sleep_stages_data,
            f"data/raw/sleep/stages/{date}.csv",
            ["start_time", "end_time", "sleep_stage"],
            look_for_duplicates=False
        )

    # SLEEP HEART RATES
    for date in date_list:
        sleep_heart_rates_data = fetch_sleep_heart_rates_data(client, date)
        save_to_csv(
            sleep_heart_rates_data,
            f"data/raw/sleep/heart_rates/{date}.csv",
            ["timestamp", "heart_rate"],
            look_for_duplicates=True
        )

    # STEPS
    steps_data = []
    for date in date_list:
        daily_steps = fetch_steps(client, date)
        steps_data.append([date, daily_steps])

    save_to_csv(
        steps_data,
        "data/raw/steps/steps.csv",
        ["date", "steps_taken"],
        look_for_duplicates=False
    )
        
    print("Data collection complete.")


if __name__ == "__main__":
    main()