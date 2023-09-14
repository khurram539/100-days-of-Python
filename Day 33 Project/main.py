#Day 33 - ISS Overhead Notifier Project

import requests
import smtplib
import datetime as dt

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# data = response.json()
# print(data)

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

