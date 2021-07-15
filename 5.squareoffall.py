from ks_api_client import ks_api
import csv
import time
from datetime import datetime
import pandas as pd
from indicator import indicators as ind



client = ks_api.KSTradeApi(access_token="8f2187b5-79a7-318d-977d-446bf4e30d71", userid="Aniket21", \
                           consumer_key="RRjAnRc8R0zf7qLIQoOlly4VS7Ya", ip="127.0.0.1", app_id="0D655C00DC3341A58568B58EF40B0EA2")


# Login using password
client.login(password="Aniket@50")

# Generate final Session Token
client.session_2fa(access_code='5722')
print(client.session_token)
print("Logged In successfully")


open = client.positions(position_type = "OPEN")
print(open)
lst = open['Success']
for element in lst :
    instrument = element['instrumentToken']
    scrip = element['instrumentName']
    openqty = element['netTrdQtyLot']

    if openqty < 0:
        client.place_order(order_type='N', instrument_token=instrument, transaction_type='BUY',
                           quantity=abs(openqty), price=0,
                           validity='GFD', variety='REGULAR')
        print(f'squared of short => {scrip}')
    elif openqty > 0:
        client.place_order(order_type='N', instrument_token=instrument, transaction_type='SELL',
                           quantity=abs(openqty), price=0,
                           validity='GFD', variety='REGULAR')
        print(f"squared of long => {scrip}")