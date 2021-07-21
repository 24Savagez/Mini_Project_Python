import requests
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "TSLA"
STOCK_API_KEY = "87XAR0KBN4JIMNI5"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "f5ad77ee10624183bc771834bc7ed159"

TWILIO_SID = 'AC796045391d4ac83f9512e3e6441dd725'
TWILIO_AUTH_TOKEN = '6536ae08a4eeb9738a824ef316acd6bf'

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Get yesterday's closing stock price.
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]

    # to send a separate message with each article's title and description to your phone number.
    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percent} %\nHeadline: {article['title']}. \nBrief: {article['description']}."
        for article in three_articles]
    # print(formatted_articles)

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+12109780151',
            to='+66985241288'
        )
        print(message.sid)
