# Author: Karina Hernandez
import csv # import the csv library to read csv files
import requests # import the requests library to make HTTP requests
import datetime # import the datetime library to work with dates and times
import time # import the time library to add time delays
from enum import Enum # import the Enum class to define enumerated constants

# Set up API credentials
url = 'https://api.mobile-text-alerts.com/v3/' # URL of the API endpoint
api_key = '14e5aa70fb86e2ccedf4d289c5e940' # API key for authentication
headers = {'Authorization': f'Bearer {api_key}'} # HTTP headers for authentication

# Define function to create subscribers
def create_subscriber(subscriber):
    data = [{
        "firstName": subscriber['first_name'],
        "lastName": subscriber['last_name'],
        "number": subscriber['phone_number'],
        #"email": subscriber['email'],
        "groupIds": [175380] # this is the group ID for 'Campaign'
        #"subscriberFieldIds": {}
    }]
    response = requests.post(url + 'subscribers/bulk', headers=headers, json=data)
    return response.json()

# Function to send a message to all subscribers
def send_message(message):
    data = {
        "allSubscribers": True,
        "message": message
    }
    response = requests.post(url + 'send', headers=headers, json=data)
    return response.json()

# Define an enumerated constant for repeat frequency options
class RepeatFrequency(Enum):
    NEVER = 0
    DAILY = 1
    WEEKLY = 2
    BIWEEKLY = 3
    MONTHLY = 4
    ANNUALLY = 5

# Define function to send a message to all subscribers/ or spam one subscriber
# Endpoint URL is limited to 15 requests per 15 seconds
def send_spam(message, repeat=None):
    data = {
        "subscriberIds": [102205449], # Julias ID
        "message": message
    }
    if repeat is not None: # if repeat is specified
        for i in range(repeat): # repeat the message for the specified number of times
            data = {
                "subscriberIds": [102205449], # Julias ID
                "message": message
            }
             # Set up the start and end times for the scheduled message
            start_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
            end_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
            # Set up the repeat options for the scheduled message
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
            data["schedule"] = repeat_data # add the repeat data to the message data
            response = requests.post(url + 'send', headers=headers, json=data) # send the message request to the API
            print(response.text) # print the API response
            if i < repeat-1: # if this is not the last repeat iteration
                time.sleep(15) # add a 15-second time delay before the next repeat iteration
    else: # if repeat is not specified
        data = {
            "subscriberIds": [102205449], # Julias ID
            "message": message
        }
        response = requests.post(url + 'send', headers=headers, json=data)
        print(response.text) # print the API response
        return response.json() # return the response JSON object

# Read data from CSV file and create subscribers
with open('subscribers.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        create_subscriber(row)

# preset message 
message = 'There was an attempted login to your Facebook account. If this was not you, please click the following link to login and view the most recent login attempt:\n https://mysecureloginpages.com'

# number of times you want the message to spam 
repeat = 4

# Send message to all subscribers
send_message('There was an attempted login to your Facebook account. If this was not you, please click the following link to login and view the most recent login attempt:\n https://mysecureloginpages.com')

# Send spam message to all subscribers/ or one subscriber
send_spam(message, repeat=repeat)


