COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "TSLA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# https://www.alphavantage.co/support/#api-key
STOCK_API_KEY = "P7FEEGDXXECQBSTM"


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
print(difference)

#T0D0 4: Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#T0D0 5: If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 5:
    print("Get News")
