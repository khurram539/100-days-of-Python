# Day 35 - API Keys, Authentication, Environment Variable
#          and Sending SMS


import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "7174a13d1a04614d1c328f63d4acbb0d"



weather_params = {
    "lat": 38.840389,
    "lon": -77.428879,
    "appid": api_key,
    
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


for hours_data in weather_slice:
   condition_code = hours_data["weather"][0]["id"]
   if int(condition_code) < 700:
       will_rain = True
if will_rain:
    print("Bring an umbrella")
       
       
# print(weather_data["hourly"][0]["weather"][0]["id"])
