import yfinance as yf
import pandas as pd
import time
import datetime;
  
# ct stores current time
ct = datetime.datetime.now()
#print("current time:-", ct)

# ts store timestamp of current time
ts = ct.timestamp()
#print("timestamp:-", ts)

stock = yf.Ticker("zim")
price = stock.info['regularMarketPrice']
hist = stock.history(period="1d", interval="1m",prepost = True, threads = True)
#print(hist)
#print(datetime.datetime.now())
print(price)

# get option chain for specific expiration
opt = stock.option_chain('2023-02-10')
# data available via: opt.calls, opt.puts
#print(opt.calls.to_string())
#stike price * 100 + premium
break_even = ((opt.calls['strike'] * 100 + opt.calls['lastPrice'] * 100) / 100)
opt.calls['breakEven'] = ((opt.calls['strike'] * 100 + opt.calls['lastPrice'] * 100) / 100)

opt.calls['impliedVolatility'] = opt.calls[(opt.calls['impliedVolatility'].clip_upper(2))]


with pd.option_context('display.max_rows', None):
    print (opt.calls)



"""
print("opt\n")
print(type(opt))
print("\n")

print("opt.calls\n")
print(type(opt.calls))
print("\n")

print("stock\n")
print(type(stock))
print("\n")
"""