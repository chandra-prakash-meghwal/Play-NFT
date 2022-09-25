import requests
import os
import time
import datetime

# https://rapidapi.com/integraatio/api/yahoofinance-stocks1/

# os.environ['rapid_api_key'] = 'rapid api key'
# os.environ['rapid_api_key'] = 'rapid api key'
os.environ['market_stack_api_key'] = 'market stack api key'
#
#
# def get_historical_prices(start_date='2020-04-01', end_date='2020-01-01', symbol='MSFT'):
#     url = "https://yahoofinance-stocks1.p.rapidapi.com/stock-prices"
#     querystring = {"EndDateInclusive": start_date,"StartDateInclusive": end_date,"Symbol": symbol,"OrderBy":"Ascending"}
#     headers = {
#         "X-RapidAPI-Key":  os.environ.get('rapid_api_key'),  # "SIGN-UP-FOR-KEY",
#         "X-RapidAPI-Host": "yahoofinance-stocks1.p.rapidapi.com"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print(response.text)
#     return response.json()


def get_historical_prices(date_from, date_to, symbol):
    """
    Documentation : https://marketstack.com/documentation
    // End-of-Day Data API Endpoint

    http://api.marketstack.com/v1/eod
        ? access_key = YOUR_ACCESS_KEY
        & symbols = AAPL

    // optional parameters:

    & sort = DESC
    & date_from = YYYY-MM-DD
    & date_to = YYYY-MM-DD
    & limit = 100
    & offset = 0
    :param date_from:
    :param date_to:
    :param symbol: e.g. MFST, CSCO
    :return: price data
    """
    url = "http://api.marketstack.com/v1/eod?access_key={}&symbols={}&date_from={}&date_to={}&limit=1&sort=ASC".format(
        os.environ.get('market_stack_api_key'), symbol, date_from, date_to
    )
    res = requests.get(url)
    print(res.status_code)
    print(res.text)
    return res.json()


def formatted_date_component(num):
    if num < 10:
        return '0{}'.format(num)
    return num


def get_health(symbol):
    unix_time_now = int(time.time())
    date_1 = datetime.datetime.utcfromtimestamp(unix_time_now - 48*60*60)
    date_2 = datetime.datetime.utcfromtimestamp(unix_time_now - 24*60*60)
    date_from = "{}-{}-{}".format(
        formatted_date_component(date_1.year),
        formatted_date_component(date_1.month),
        formatted_date_component(date_1.day)
    )
    date_to = "{}-{}-{}".format(
        formatted_date_component(date_2.year),
        formatted_date_component(date_2.month),
        formatted_date_component(date_2.day)
    )
    print(date_from, date_to)
    price_data = get_historical_prices(date_from=date_from, date_to=date_to, symbol=symbol)
    try:
        open_price = price_data['data'][0]['open']
        close_price = price_data['data'][0]['close']
        print(open_price, close_price, type(open_price), type(close_price))
        diff_price = close_price - open_price
        print(diff_price)
        health = int(100 * 100 * diff_price // open_price)  # rounded to the nearest integer
    except:
        health = 0  # api do not support the particular stock symbol

    return health
