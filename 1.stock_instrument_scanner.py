import requests
from datetime import date,timedelta
import os

today = (date.today()).strftime("%d_%m_%Y")
print(today)
stocks = ['HDFCBANK','ADANIENT','TATASTEEL','SBICARD','AXISBANK','JSWSTEEL','ADANIPORTS','HDFCLIFE','ICICIBANK','WIPRO','JINDALSTEL','BHARATIARTL','HINDALCO','MOTHERSUMI','INFY']
expiry ="15JUL21"
strikes = ['15800CE','15850PE']
# instrumentToken|instrumentName|name|lastPrice|expiry|strike|tickSize|lotSize|instrumentType|segment|exchange|isin|multiplier|exchangeToken|optionType
# ['15130', 'BANKNIFTY', '', '4219.65', '01JUL21', '39600', '0.050000', '25', 'OI', 'FO', 'NSE', '', '1', '38432', 'PE']
# print(len(stocks))
l2 = []
def get_instrument_dict():
    r = requests.get("https://preferred.kotaksecurities.com/security/production/TradeApiInstruments_CASH_"+today+".txt")
    # print(r)
    r = r.text.split("\n")
    # print(r)
    l=[]
    for i in r:
        for stock in stocks:
            # print(stock)
            if stock in i and "NSE" in i :
                # print(i)
                l.append((i.split('|')))
                # print(len(l))
    d={}
    for stock in stocks:
        for i in l:
            scrip = i[1]  # "BANKNIFTY01JUL2139600PE" : 15130
            # print(scrip)
            if stock == scrip:
                d[scrip]= i[0]
                l2.append(int(d[scrip]))

    print(l2)
    print(d)
    return d

get_instrument_dict()