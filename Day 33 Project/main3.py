# Match Sunset and Sunrise times in the same day

import requests
from datetime import datetime



MY_LAT = 38.840031
MY_LONG = -77.423172


Parameters = {
    "lats": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}       
    
response = requests.get("https://api.sunrise-sunset.org/json", params=Parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)




