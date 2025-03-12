import pandas as pd
import requests
import newsapi.articles
import newsapi.sources

if __name__ == '__main__':
    # Alpha Vantage API details
    API_KEY = " VEV44TIRFGC4AVR7"
    NEWS_API_KEY = "13da08efebbe49beba70c1cc894c066d"
    SYMBOL = "BTC"  # Replace with your stock symbol
    DAY = 0
    TIME = ["TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_MONTHLY"]
    TIME_DAY = ["Time Series (Daily)", "Weekly Time Series", "Monthly Time Series"]
    ALPHA_URL = f"https://www.alphavantage.co/query?function={TIME[DAY]}&symbol={SYMBOL}&apikey={API_KEY}&outputsize=compact"
    NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"
    LAST_X = 10

    # Fetch stock data
    response = requests.get(ALPHA_URL)
    data = response.json()

    # Extract closing prices
    time_series = data.get(TIME_DAY[DAY], {})
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df = df.rename(columns={"4. close": "Close Price"})[["Close Price"]]
    df.index = pd.to_datetime(df.index)
    df = df.sort_index().tail(LAST_X)  # Get the last (days,weeks,months)

    print(df)

    # Use this to get resources to give to articles
    # sources = newsapi.sources.Sources(API_KEY=NEWS_API_KEY)
    # sources.get(category='business', language='en', country='us')

    article = newsapi.articles.Articles(API_KEY=NEWS_API_KEY)
    print(article.get(source="bloomberg"))

    # Save to Excel
    # excel_filename = "stock_prices.xlsx"
    # df.to_excel(excel_filename, sheet_name="Stock Data")
    #
    # print(f"Stock data saved to {excel_filename}. You can upload this file to Google Sheets.")
