import yfinance as yf
import plotly.graph_objs.scatter.Line as go
from stockstats import StockDataFrame

appl = yf.Ticker("AAPL")

# get stock info
ts = (
    appl.history("1y")
    .reset_index()
    .pipe(lambda d: d.rename(columns={c: c.lower() if c != "Date" else "datetime" for c in d.columns}))
)

fig = go.Figure(data=[go.Candlestick(x=ts['datetime'],
                                         open=ts['open'],
                                         high=ts['high'],
                                         low=ts['low'],
                                         close=ts['close'],
                                         line=dict(width=1))])


df_ti = StockDataFrame.retype(ts)
technical_indicator = "close_10_sma"
fig.add_trace(go.Line(x=df_ti['datetime'],y=df_ti[technical_indicator],))