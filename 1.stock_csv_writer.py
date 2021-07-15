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
watchlist = [1250, 729, 2094, 62034, 2302, 4267, 9077, 36027, 1324, 2211, 3087, 1271, 1617, 1375]

#{'HDFCBANK': '1250', 'ADANIENT': '729', 'TATASTEEL': '2094', 'SBICARD': '62034', 'AXISBANK': '2302',
# 'JSWSTEEL': '4267', 'ADANIPORTS': '9077', 'HDFCLIFE': '36027', 'ICICIBANK': '1324', 'WIPRO': '2211',
# 'JINDALSTEL': '3087', 'HINDALCO': '1271', 'MOTHERSUMI': '1617', 'INFY': '1375'}

now = datetime.now().strftime("%H/%M/%S")
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
        scrip = m['stk_name']
        now = datetime.now().strftime("%d/%m/%Y")
        row = [t1me,scrip,ltp,vol]

        with open(f'{instrument}.csv','a',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)

            # time.sleep(0.5)