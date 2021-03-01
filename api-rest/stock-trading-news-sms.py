import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "sr34ff34"
NEWS_API_KEY = "sbfih3f34erifh4"

TWILIO_SID = '' 
TWILIO_AUTH_TOKEN = ''

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
# response.raise_for_exceptions()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]['4. close']
day_before_yesterday_closing_price = data_list[1]['4. close']
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
  up_down = '🔺'
else:
  up_down = '🔻'

diff_percent = round(difference / float(yesterday_closing_price)) * 100

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator
if diff_percent > 1:
    print("GET NEWS")
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qlnTitle': COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = response.json()['articles']
    three_articles = news_data[:3]



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.
formatted_articles = [f'{STOCK}: {up_down}{diff_percent}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]


# proxy client required for hosting this code to run as PythonAnywhere Cloud job
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
for article in formatted_articles: 
    message = client.messages \
        .create(
        body=article,
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
print(message.status)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

