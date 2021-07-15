from ks_api_client import ks_api
import time
import pandas as pd
from indicator import indicators as ind

client = ks_api.KSTradeApi(access_token="8f2187b5-79a7-318d-977d-446bf4e30d71", userid="Aniket21", \
                           consumer_key="RRjAnRc8R0zf7qLIQoOlly4VS7Ya", ip="127.0.0.1", app_id="0D655C00DC3341A58568B58EF40B0EA2")

# Login using password
client.login(password="Aniket@50")

# Generate final Session Token
client.session_2fa(access_code='6583')
print(client.session_token)
print("Logged In successfully")

#Starting Statements
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(f'Started @ {current_time}')
timeframe = '3Min'
print("Retriving Data...... for watchlist")
traded_scripts = []
long_scrips = {}
short_Scrips = {}
watchlist = [28551, 28553, 28558, 28560]
#{'NIFTY15JUL2115850CE\r': '28551', 'NIFTY15JUL2115900CE\r': '28553', 'NIFTY15JUL2115950PE\r': '28558', 'NIFTY15JUL2116000PE\r': '28560'}

gain = 0
Trades = 0
Complete_Trades = 0
open_gain = 0
profitable = 0
losing = 0
diff = [0]
qty = 300
counted_trades = 0
def charges(qty,entry,exit):
    stt = 0.0005*exit*qty
    ts = 0.0005 * (exit + entry) * qty
    sc = 0.00003 * entry * qty
    tot = stt + ts + sc
    ipf = 0.00001 * (exit + entry) * qty
    return tot

while True:
    if Trades != counted_trades :
        set(diff)
        max_gain = max(diff)
        max_loss = min(diff)
        print(f"Gains = {gain}")
        print(f"No. of Trades = {Trades}")
        print(f"Completed Trades = {Complete_Trades}")
        # print(f"Open gain = {open_gain} for scrip = {scrip}")
        print(f"No. of Profitable Trades = {profitable}")
        print(f'NO of Losing Trades = {losing}')
        print(f"Max Gain = {max_gain}")
        print(f'Max Loss = {max_loss}')
        counted_trades = Trades
        try:
            print(f"Avg = {gain / Complete_Trades}")
        except Exception as f:
            pass
        print("------------------------------------------------------------")

    else:
        pass


    for instrument in watchlist:
        # data from quote restructuring
        w = (client.quote(instrument))
        k = (w['success'])
        m = k[0]

        if instrument == 28551:
            scrip = 'NIFTY15850CE'
        elif instrument == 28553:
            scrip = 'NIFTY15900CE'
        elif instrument == 28558:
            scrip = 'NIFTY15950PE'
        elif instrument == 28560:
            scrip = 'NIFTY16000PE'


        df = pd.read_csv(f"{instrument}.csv",names=['Time','Scrip','LTP','Vol'],index_col=0,parse_dates=True)
        df = pd.DataFrame(df)
        ohlc = df['LTP'].resample(timeframe).ohlc()
        ohlc['scrip'] = scrip
        ha = ind.HA(df=ohlc,ohlc=['open','high','low','close'])
        sup = ind.SuperTrend(ha, 2, 0.7, ohlc=['HA_open', 'HA_high', 'HA_low', 'HA_close'])
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 200)
        sup['scrip'] = scrip
        # print(sup)
        # print(scrip)

        try :
            current_candle = sup.iloc[-1]
            last_candle = sup.iloc[-2]
            second_last_candle = sup.iloc[-3]
            third_last_candle = sup.iloc[-4]
            fourth_last_candle = sup.iloc[-5]
            third_candle = sup.iloc[2]
            fourth_candle = sup.iloc[3]
            fifth_candle = sup.iloc[4]
            sixth_candle = sup.iloc[5]
            current_close = round(0.05 * round(current_candle['HA_close'] / 0.05), 2)
            ha_close = round(0.05 * round(last_candle['HA_close'] / 0.05), 2)
            ha_close2 = round(0.05 * round(second_last_candle['HA_close'] / 0.05), 2)
        except Exception as e:
            pass

        # adding time to scrip
        time_local = time.localtime()
        currentT = time.strftime("%H:%M:%S", time_local)

        try:
            if ha_close == 0:
                exit()

            long_condition = ((last_candle['STX_2_0.7'] == 'up') and \
                             (second_last_candle['STX_2_0.7'] == 'down') and\
                             (f'{scrip}' not in long_scrips))

            short_condition = ((last_candle['STX_2_0.7'] == 'down') and\
                              (second_last_candle['STX_2_0.7'] == 'up') and\
                              (f'{scrip}' not in short_Scrips))


            ##LONG SIGNAL
            if long_condition:
                print(f"Buy => {scrip} at {ha_close} with prev_candle = {ha_close2}, sup = {round((last_candle['ST_2_0.7']), 2)} and last_sup = {round((second_last_candle['ST_2_0.7']), 2)} on {currentT}")
                long_scrips[f'{scrip}'] = ha_close
                Trades = Trades + 1
                # client.place_order(order_type='N', instrument_token=instrument, transaction_type='BUY', quantity=qty,
                #                    price=ha_close,
                #                    validity='GFD', variety='REGULAR')
                print('orderplaced')


            ##short Signal
            if short_condition :

                if f'{scrip}' in long_scrips:
                    diff_L = float(ha_close) - float(long_scrips[f'{scrip}'])
                    if diff_L >= 0:
                        profitable = profitable + 1
                    else:
                        losing = losing + 1
                    diff.append(diff_L)
                    Trades = Trades + 1
                    Complete_Trades = Complete_Trades + 1
                    print(f"bought @ = {float(long_scrips[f'{scrip}'])} sold @ = {float(ha_close)}")
                    print(f"Squared OFF Long => {scrip} at {ha_close} on {currentT} with Gain = {diff_L}... ")
                    charge = charges(qty=qty, entry=float(long_scrips[f'{scrip}']), exit=ha_close)
                    brokerage = brokerage + charge
                    gain = gain + (diff_L - charge)*qty
                    long_scrips.pop(f'{scrip}')
                    # client.place_order(order_type='N', instrument_token=instrument, transaction_type='SELL',
                    #                    quantity= qty, price= ha_close,
                    #                    validity='GFD', variety='REGULAR')
                    print('Order_placed')

        except Exception as e:
            pass
