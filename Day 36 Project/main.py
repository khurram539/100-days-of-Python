#Stock News Project

import requests
from twilio.rest import Client

# Company name and stock symbol
COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "TSLA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# https://www.alphavantage.co/support/#api-key
STOCK_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NEWS_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_SID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

#T0D0 1: Get yesterday's closing stock price. 
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#T0D0 2:  Get the day before yesterday's closing stock price. Hint: You can slice lists.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#T0D0 3: Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#T0D0 4: Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

#T0D0 5: If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percent > 5:
#     print("Get News")
    
#T0D0 6: Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
        
news_response =  requests.get(NEWS_ENDPOINT, params=stock_params)
articles = (news_response.json()["articles"])
print(articles)

#T0D0 7: Use Python slice operator to create a list that contains the first 3 articles.
three_articles = articles[:3]
print(three_articles)

#T0D0 8: Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+xxxxxxxxxxx',
        to='+xxxxxxxxxxx'
    )
    print(message.status)


