import urllib
import json
import requests
import csv
import time
import os
import cv2
import keyboard

if os.path.exists(str(os.path.dirname(os.path.realpath(__file__))) + "/CoinMarketCapData.csv"):

    coin_data = open('CoinMarketCapData.csv', "a", newline='')
    csvwriter = csv.writer(coin_data)
else:
    coin_data = open('CoinMarketCapData.csv', "w", newline='')
    csvwriter = csv.writer(coin_data)
    columnTitleRow = ['current_time', 'coin_id', 'symbol', 'price_usd', 'market_cap_usd', 'percent_change_1h',
                      'percent_change_24h', 'percent_change_7d']
    csvwriter.writerow(columnTitleRow)

main_api = 'https://api.coinmarketcap.com/v1/ticker/'

coins = ['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash', 'litecoin', 'monero', 'iota', 'stellar', 'raiblocks',
         'siacoin']
i=0
while i < 1000:
    for coin in coins:
        url = main_api + coin
        print(url)
        json_data = requests.get(url).json()
        print(json_data)

        # get information wanted
        current_time = time.strftime("%Y-%m-%d %H:%M")
        coin_id = json_data[0]['id']
        symbol = json_data[0]['symbol']
        price_usd = json_data[0]['price_usd']
        market_cap_usd = json_data[0]['market_cap_usd']
        percent_change_1h = json_data[0]['percent_change_1h']
        percent_change_24h = json_data[0]['percent_change_24h']
        percent_change_7d = json_data[0]['percent_change_7d']
        # print(coin_id)

        data_list = [current_time, coin_id, symbol, price_usd, market_cap_usd, percent_change_1h, percent_change_24h,
                     percent_change_7d]

        csvwriter.writerow(data_list)
    coin_data.flush()
    os.fsync(coin_data.fileno())
    print('Saved Data!')
    i += 1
    time.sleep(600)
