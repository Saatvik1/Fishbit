import fitbit
import requests
import time
import oauth2
import pprint
import json
import csv
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()


#print(os.getenv("ACCESS_TOKEN")) 

# get_activities_url = f'https://api.fitbit.com/1/user/{CLIENT_ID}/activities/list.json'
get_activities_url = f'https://api.fitbit.com/1/user/-/activities/list.json'

get_activities_param = {
    'beforeDate' : '2024-07-17',
    'sort' : 'asc',
    'limit' : 100,
    'offset' : 0
}
get_activities_headers = {
    "authorization" : f"Bearer {os.getenv('ACCESS_TOKEN')}"
}

activities_req = requests.get(url = get_activities_url, params=get_activities_param, headers=get_activities_headers)

activities_json = activities_req.json()

print(activities_json)
