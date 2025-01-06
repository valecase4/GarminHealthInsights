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

def fetch_sleep_data_stages(client, date):
    stages = {
        1: "Deep",
        2: "Light",
        3: "REM",
        0: "Awake"
    }
    try:
        data = client.get_sleep_data(date)['sleepHeartRate']
        sleep_data_stages = []
        for record in data:
            print(record)
            # start_gmt_time = datetime.strptime(record['startGMT'], "%Y-%m-%dT%H:%M:%S.%f")
            # start_local_time = (start_gmt_time + timedelta(hours=1)).strftime("%H:%M")
            # end_gtm_time = datetime.strptime(record['endGMT'], "%Y-%m-%dT%H:%M:%S.%f")
            # end_local_time = (end_gtm_time + timedelta(hours=1)).strftime("%H:%M")
            # sleep_stage = stages[int(record['activityLevel'])]

            # print([start_local_time, end_local_time, sleep_stage])

            # sleep_data_stages.append([start_local_time, end_local_time, sleep_stage])

        print(f"Sleep data retrieved for {date}.")
        # return sleep_data_stages
    except Exception as e:
        print(f"Error fetching sleep data: {e}")
        return None
    
# sleepLevels
# sleepHeartRate

if __name__ == '__main__':
    client = authenticate()

    fetch_sleep_data_stages(client, date='2025-01-06')


    # for record in sleep_data:
    #     print(record)

    # print(sleep_data)