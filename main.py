import binance_endpoints
from time import time, sleep
import os
import sys

import requests



ticker = 'USDT'

bot_id = os.environ['telegram_bot_key']
chat_id = os.environ['telegram_chat_id']


base_url  = f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text='


try:
    while True:

        ticker_pairs = binance_endpoints.all_ticker_pairs(ticker)

        if not os.path.isfile(ticker):
            binance_endpoints.overwrite_previous_list(ticker, ticker_pairs)


        stored_pairs = binance_endpoints.read_previous_list(ticker)
        new_coins = binance_endpoints.compare_lists(stored_pairs, ticker_pairs)

        if len(new_coins):

            requests.get(base_url + '"' + str(new_coins).replace('[','').replace(']','').replace("'", "") + '"')

            print(base_url + str(new_coins).replace('[','').replace(']','').replace("'", "").replace(" ", ","))
            binance_endpoints.overwrite_previous_list(ticker, ticker_pairs)

            print("sent coin names")
            print(new_coins)

        else:
            pass
            print("No new coins")
        sleep(15)
except:
    requests.get(base_url + "Process has failed")
    sys.exit()

