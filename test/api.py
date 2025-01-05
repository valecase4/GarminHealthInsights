from garminconnect import Garmin
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

try:
    # Test Authentication
    client = Garmin(email, password)
    client.login()
    print("Connection Successful!")

    # Test API call
    activities = client.get_activities(start=0, limit=1)
    print("Sample activity: ", activities)
except Exception as e:
    print("Error during connection:", e)