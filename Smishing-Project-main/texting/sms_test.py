# Author: Karina Hernandez
import requests
import datetime
import time
from enum import Enum

# Set up API credentials
url = 'https://api.mobile-text-alerts.com/v3/'
api_key = '14e5aa70fb86e2ccedf4d289c5e940'
headers = {'Authorization': f'Bearer {api_key}'}

class RepeatFrequency(Enum):
    NEVER = 0
    DAILY = 1
    WEEKLY = 2
    BIWEEKLY = 3
    MONTHLY = 4
    ANNUALLY = 5

# Define function to send a message to all subscribers
def send_spam(message, repeat=None):
    data = {
        "subscriberIds": [102205449], # Julias ID
        "message": message
    }
    if repeat is not None:
        for i in range(repeat):
            data = {
                "subscriberIds": [102205449], # Julias ID
                "message": message
            }
            start_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            end_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
            repeat_data = {
                "startDate": start_time,
                "endDate": end_time,
                "repeat": {
                    "monday": True,
                    "tuesday": True,
                    "wednesday": True,
                    "thursday": True,
                    "friday": True,
                    "saturday": False,
                    "sunday": False,
                    "type": "week",
                    "frequency": RepeatFrequency.NEVER.value
                },
                "repeatTimes": 1
            }
            data["schedule"] = repeat_data
            response = requests.post(url + 'send', headers=headers, json=data)
            print(response.text)
            if i < repeat-1:
                time.sleep(15)
    else:
        data = {
            "subscriberIds": [102205449], # Julias ID
            "message": message
        }
        response = requests.post(url + 'send', headers=headers, json=data)
        print(response.text)
        return response.json()


message = 'Hi I am testing sending repeated messages. https://mysecureloginpages.com'
repeat = 4
# Send message to all subscribers
send_spam(message, repeat=repeat)

