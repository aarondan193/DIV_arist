from multiprocessing.sharedctypes import Value
import yfinance as yf


import pandas as pd
from yahoo_fin import stock_info as si


# gather stock symbols from major US exchanges
df1 = pd.DataFrame( si.tickers_sp500() )
df2 = pd.DataFrame( si.tickers_nasdaq() )
df3 = pd.DataFrame( si.tickers_dow() )
#df4 = pd.DataFrame( si.tickers_other() )

# convert DataFrame to list, then to sets
sym1 = set( symbol for symbol in df1[0].values.tolist() )
sym2 = set( symbol for symbol in df2[0].values.tolist() )
sym3 = set( symbol for symbol in df3[0].values.tolist() )
#sym4 = set( symbol for symbol in df4[0].values.tolist() )

# join the 4 sets into one. Because it's a set, there will be no duplicate symbols
symbols = set.union( sym1, sym2, sym3 )

# Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
my_list = ['W', 'R', 'P', 'Q']
del_set = set()
sav_set = set()

for symbol in symbols:
    if len( symbol ) > 4 and symbol[-1] in my_list:
        del_set.add( symbol )
    else:
        sav_set.add( symbol )

#print( f'Removed {len( del_set )} unqualified stock symbols...' )
print( f'There are {len( sav_set )} qualified stock symbols...' )

#for line in sav_set:
#    line = line.strip()
#    print (line)
#    ticker = yf.Ticker(line)
#    data = ticker.history(period="1y")
#    try:
#        last_quote = data['Close'].iloc[-1]
#        print (last_quote)
#    except:
#        print ("exception")
    





f = open(r"C:\Users\14407\OneDrive\Desktop\div_arist\div_ari.txt", "r")

divArist = {}
for line in f.readlines():
    line = line.strip()
    ticker = yf.Ticker(line)
    data = ticker.history(period="1y")
    last_quote = data['Close'].iloc[-1]

    
    
    div = ticker.actions
    div = div['Dividends'].sum()
    
    percent = round(div / last_quote * 100, 2)
    
    divArist[line] = percent
    


sorteddict = dict(sorted(divArist.items(), reverse=True, key=lambda item: item[1]))

for k, v in sorteddict.items():
    print(str(k) + " " + str(v))

print(sorteddict)


#get all tickers
#download data
#PE ratio
#price to book ratio
#debt to equity ratio
#free cash flow
#peg ratio