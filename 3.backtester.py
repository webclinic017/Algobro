from ks_api_client import ks_api
import time
import pandas as pd
from indicator import indicators as ind



client = ks_api.KSTradeApi(access_token="8f2187b5-79a7-318d-977d-446bf4e30d71", userid="Aniket21",
                           consumer_key="RRjAnRc8R0zf7qLIQoOlly4VS7Ya", ip="127.0.0.1", app_id="0D655C00DC3341A58568B58EF40B0EA2")


# Login using password
client.login(password="Aniket@50")

# Generate final Session Token
client.session_2fa(access_code='6583')
print(client.session_token)
print("Logged In successfully")


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('Started' + ' @ ' + current_time)

timeframe = '3Min'
print((f'Current Timeframe = {timeframe}'))
print("Retriving Data...... for watchlist")
traded_scripts = []
long_scrips={}
short_Scrips={}
watchlist =[1250, 729, 2094, 62034, 2302, 4267, 9077, 36027, 1324, 2211, 3087, 1271, 1617, 1375]
#{'HDFCBANK': '1250', 'ADANIENT': '729', 'TATASTEEL': '2094', 'SBICARD': '62034', 'AXISBANK': '2302',
# 'JSWSTEEL': '4267', 'ADANIPORTS': '9077', 'HDFCLIFE': '36027', 'ICICIBANK': '1324', 'WIPRO': '2211',
# 'JINDALSTEL': '3087', 'HINDALCO': '1271', 'MOTHERSUMI': '1617', 'INFY': '1375'}
gain= 0
counted_Trades = 0
Trades = 0
brokerage = 0
qty = 10
profitable = 0
losing = 0

def charges(qty,entry,exit):
    stt = 0.00025*exit*qty
    ts = 0.00003253 * (exit + entry) * qty
    sc = 0.00003 * entry * qty
    tot = stt + ts + sc
    return tot


# def probablity (diff,charge):
#     if diff - charge >= 0:
#         profitable = profitable + 1
#     else:
#         losing = losing + 1


while True:
    if Trades > counted_Trades:
        print('-------------------------------------------------------------------')
        print(f"Gains = {gain}")
        print((f"No. of Trades = {Trades}"))
        try:
            print(f"Avg = {gain/Trades}")
        except Exception as f:
            pass
        print(f'NO of Profitable Trades = {profitable}')
        print(f'No.of Losing trades = {losing}')
        # print(f"test counted trades = {counted_Trades}")
        print('-------------------------------------------------------------------')
        counted_Trades = Trades
    for instrument in watchlist:
        ##data from quote restructuring
        w = (client.quote(instrument))
        k = (w['success'])
        m = k[0]
        scrip = m['stk_name']
        df = pd.read_csv(f"{instrument}.csv",names=['Time', 'Scrip', 'LTP', 'Vol'], index_col=0, parse_dates=True)
        df = pd.DataFrame(df)
        ohlc = df['LTP'].resample(timeframe).ohlc()
        ohlc['scrip'] = scrip
        ha = ind.HA(df=ohlc, ohlc=['open', 'high', 'low', 'close'])
        sup = ind.SuperTrend(ha, 2, 0.7, ohlc=['HA_open', 'HA_high', 'HA_low', 'HA_close'])
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 200)
        sup['scrip'] = scrip
        # print(sup)

        try:
            current_candle = sup.iloc[-1]
            last_candle = sup.iloc[-2]
            second_last_candle = sup.iloc[-3]
            third_last_candle = sup.iloc[-4]
            fourth_last_candle = sup.iloc[-5]
            third_candle = sup.iloc[2]
            fourth_candle = sup.iloc[3]
            fifth_candle = sup.iloc[4]
            sixth_candle = sup.iloc[5]
            ha_close = round(0.05 * round(last_candle['HA_close'] / 0.05), 2)
        except Exception as e:
            print(e)
            pass


        # adding time to scrip
        time_local = time.localtime()
        currentT = time.strftime("%H:%M:%S", time_local)

        try:
            if ha_close == 0:
                exit()
            else:
                pass

            long_condition = ((last_candle['STX_2_0.7'] == 'up') and
                             (second_last_candle['STX_2_0.7'] == 'down') and
                             (f'{scrip}' not in long_scrips))
            short_condition = ((last_candle['STX_2_0.7'] == 'down') and
                              (second_last_candle['STX_2_0.7'] == 'up') and
                              (f'{scrip}' not in short_Scrips))
            ##LONG SIGNAL
            if long_condition:
                print(f" buy => {scrip} at {ha_close} with sup = {round((last_candle['ST_2_0.7']), 2)} and last sup = {round((second_last_candle['ST_2_0.7']), 2)} on {currentT}")
                long_scrips[f'{scrip}'] = ha_close
                # client.place_order(order_type='MIS', instrument_token=instrument, transaction_type='BUY', quantity=qty,
                #                    price= ha_close,
                #                    validity='GFD', variety='REGULAR')
                print('orderplaced')
                if f'{scrip}' in short_Scrips:
                    diff_S = float(short_Scrips[f'{scrip}']) - float(ha_close)
                    gain = gain + diff_S
                    Trades = Trades + 1
                    print(f"Squared OFF Short => {scrip} at {ha_close} on {currentT}  with Gain = {diff_S}....")
                    charge  = charges(qty=qty,entry=float(short_Scrips[f'{scrip}']),exit=ha_close)
                    brokerage = charge + brokerage
                    gain = gain + diff_S - charge
                    short_Scrips.pop(f'{scrip}')
                    # probablity(diff= diff_S,charge=charge)
                    # client.place_order(order_type='MIS', instrument_token=instrument, transaction_type='BUY',
                    #                    quantity=qty,price= ha_close,
                    #                    validity='GFD', variety='REGULAR')
                    print('orderplaced')
                    if (diff_S-charge) >= 0:
                        profitable = profitable+1
                    else:
                        losing = losing+1
            ##short Signal
            if short_condition :
                print(f" sell => {scrip} at {ha_close} on {currentT}")
                short_Scrips[f'{scrip}'] = ha_close
                # client.place_order(order_type='MIS', instrument_token=instrument, transaction_type='SELL', quantity=qty,
                #                    price=ha_close,
                #                    validity='GFD', variety='REGULAR')
                print('Order Placed')
                if f'{scrip}' in long_scrips:
                    diff_L = float(ha_close) - float(long_scrips[f'{scrip}'])
                    Trades = Trades + 1
                    print(f"bought @ = {float(long_scrips[f'{scrip}'])} sold @ = {float(ha_close)}")
                    print(f"Squared OFF Long => {scrip} at {ha_close} on {currentT} with Gain = {diff_L}... ")
                    charge = charges(qty=qty, entry=float(long_scrips[f'{scrip}']), exit=ha_close)
                    brokerage = brokerage + charge
                    # probablity(diff=diff_L, charge=charge)
                    gain = gain + diff_L - charge
                    long_scrips.pop(f'{scrip}')
                    # client.place_order(order_type='MIS', instrument_token=instrument, transaction_type='SELL',
                    #                    quantity=qty, price=ha_close,
                    #                    validity='GFD', variety='REGULAR')
                    print('Order Placed')
                    if (diff_L - charge) >= 0:
                        profitable = profitable+1
                    else:
                        losing = losing+1

        except Exception as e:
            print(e)
            pass

