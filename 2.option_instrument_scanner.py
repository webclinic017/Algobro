import requests
from datetime import date,timedelta
import os

today = (date.today()).strftime("%d_%m_%Y")
print(today)

# expiry = os.getenv("EXP")
expiry ="15JUL21"
strikes = ['15850CE','15950PE','15900CE','16000PE']
# instrumentToken|instrumentName|name|lastPrice|expiry|strike|tickSize|lotSize|instrumentType|segment|exchange|isin|multiplier|exchangeToken|optionType
# ['15130', 'BANKNIFTY', '', '4219.65', '01JUL21', '39600', '0.050000', '25', 'OI', 'FO', 'NSE', '', '1', '38432', 'PE']
l2 = []
def get_instrument_dict():
    r = requests.get("https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_FNO_"+today+".txt")
    # print(r)
    r = r.text.split("\n")
    # print(r)
    l=[]
    for i in r:
        if expiry in i and "NIFTY" in i and "BANKNIFTY" not in i and "FINNIFTY" not in i:
            l.append(i.split('|'))
    d={}
    for i in l:
        scrip = i[1]+i[4]+i[5]+i[14]  # "BANKNIFTY01JUL2139600PE" : 15130
        for strike in strikes:
            if strike in scrip:
                d[scrip]= i[0]
                l2.append(int(d[scrip]))
    print(d)
    print(l2)

    return d

get_instrument_dict()