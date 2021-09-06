from binance.client import Client
import os
#import json
import numpy as np


# requires environment variables to be set prior to use
client = Client(os.environ['binance_key'], os.environ['binance_secret'])



def all_ticker_pairs(ticker: str):
    """
    returns a list object with all of the listed ticker pairs available
    """

    response = client.get_exchange_info()
    all_pairs = response['symbols']
    ticker_pairs = [pair for pair in all_pairs if ticker in pair['symbol']]
    obj = {"data": ticker_pairs}

    # Remove ticker name from pair to just show target coin
    data = [x['symbol'].replace(ticker, "") for x in obj['data']]

    return data



def overwrite_previous_list(filename: str, list: list):
    """
    writes list to a file with each list object
    appearing on a new line
    """
    with open(filename, "w") as f:
        f.write("\n".join(list))


def read_previous_list(filename: str):
    """
    Opens the previously held list of pairs, used
    for comparison with the results from the 
    all_ticker_pairs function 
    """

    with open(filename) as f:
        data = f.read()
        data = data.split("\n")

    return data


def compare_lists(stored: list, new_request: list):
    """
    Compares the current stored list of available trade pairs
    with the result set from the new request
    """

    new_coins = np.setdiff1d(new_request, stored)

    return new_coins



if __name__ == '__main__':

    print(all_ticker_pairs('USDT'))