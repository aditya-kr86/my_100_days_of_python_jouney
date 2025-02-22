import requests
import smtplib

MY_EMAIL = "MY_EMAIL"
MY_PASSWORD = "MY_PASSWORD"
recipient_email = "recipient_email"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_key = "API_key"
NEWS_API = "NEWS_API"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_key
}
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
#When stock price increase/decreases by 5% between yestarday and the day before yesterday then
r = requests.get(STOCK_ENDPOINT, params=stock_params)
data = r.json()
# print(data)
trade_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in trade_data.items()]

#TODO 1. - Get yestarday's closing stock price
yestarday_closing_price = data_list[0]['4. close']
# print(yestarday_closing_price)

#TODO 2. - Get the day before yestarday's closing stock price
db_yestarday_closing_price = data_list[1]['4. close']
# print(db_yestarday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2.e.g. 40 - 20 = -20,but the positive  is 20. https://www.w3school.com
up_down = None
difference = (float(yestarday_closing_price) -
              float(db_yestarday_closing_price))
if difference > 0:
	up_down = "High"
elif difference < 0:
	up_down = "Low"
# print(difference)

#TODO 4. - Work out the value of 5% of yestarday's closing price
diff_percent = (abs(difference) / float(yestarday_closing_price)) * 100
# print(diff_percent)

#TODO 5. - If TODO4 is true then print("Get News").
if diff_percent:
	print("Getting News\n")

## STEP 2: Instead of printing ("Get News"),actually get the first 3 news pieces for the COMPANY
#TODO 6.- Use Python slice operator to create a list that contains the first 3 articles, Hint: https://stackoverflow.com/questions/509211/how-slicing-in-python-works
if diff_percent > 1:
	news_params = {"apikey": NEWS_API, "qInTitle": COMPANY_NAME}
	news_response = requests.get(NEWS_ENDPOINT, params=news_params)
	news_data = news_response.json()["articles"][:3]

	#TODO 7.- Create a new list of the first 3 article's headline and description using list comprehension.
	news_list = [
	    f"{STOCK_NAME}:{up_down}{difference:.2f}%.\nHeadline: {news['title']}.\nBrief: {news['description']}"
	    for news in news_data
	]

	#TODO 8.- Send each article as a seperate message via Twilio.
	with smtplib.SMTP("smtp.gmail.com", 587) as connection:
		connection.starttls()
		connection.login(MY_EMAIL, MY_PASSWORD)
		for news in news_list:
			connection.sendmail(
			    from_addr=MY_EMAIL,
			    to_addrs=recipient_email,
			    msg=f"Subject:{COMPANY_NAME} : {difference:.2f}%\n\n{news}")
			print(news)
			print("\n")
		if connection:
			try:
				print("Email's Sent Sucessfully")
				connection.quit()  # Close the connection
			except smtplib.SMTPServerDisconnected:
				print("Email's Sent Sucessfully")
				print("The connection was already closed.")
