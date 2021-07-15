from ks_api_client import ks_api
import csv
import time
from datetime import datetime

client = ks_api.KSTradeApi(access_token="8f2187b5-79a7-318d-977d-446bf4e30d71", userid="Aniket21", \
                           consumer_key="RRjAnRc8R0zf7qLIQoOlly4VS7Ya", ip="127.0.0.1", app_id="0D655C00DC3341A58568B58EF40B0EA2")


# Login using password
client.login(password="Aniket@50")

# Generate final Session Token
client.session_2fa(access_code='6583')
print(client.session_token)
print("Logged In successfully")
watchlist = [28551, 28553, 28558, 28560]
#{'NIFTY15JUL2115850CE\r': '28551', 'NIFTY15JUL2115900CE\r': '28553', 'NIFTY15JUL2115950PE\r': '28558', 'NIFTY15JUL2116000PE\r': '28560'}


now = datetime.now().strftime("%d/%m/%Y")
print(f"Started @ {now}")


# print(client.quote(instrument))
while True:

    for instrument in watchlist:
        w = (client.quote(instrument))
        k = (w['success'])
        m = k[0]
        last_traded_datetime = m['BD_last_traded_time']
        last_traded_time = last_traded_datetime.split(" ")[1]
        vol = m['last_trade_qty']
        ltp = float(m['ltp'])
        t1me = datetime.strptime(last_traded_datetime, '%d/%m/%Y %H:%M:%S')

        if instrument == 28551:
            scrip = 'NIFTY15850CE'
        elif instrument == 28553:
            scrip = 'NIFTY15900CE'
        elif instrument == 28558:
            scrip = 'NIFTY15950PE'
        elif instrument == 28560:
            scrip = 'NIFTY16000PE'
        # scrip = m['stk_name']

        row = [t1me,scrip,ltp,vol]

        with open(f'{instrument}.csv','a',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

            # time.sleep(0.5)