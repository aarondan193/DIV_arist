# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

import plotly.graph_objs as go

#Interval required 1 minute
data = yf.download(tickers='googl', period='1d', interval='1m')
datahead = data
data = data.resample('15min').mean()


#declare figure
fig = go.Figure(go.Scatter(
    x = datahead.index,
    y = datahead['Close'],
    name='1 minute marker'
))

fig2 = go.Figure(go.Scatter(
    x = data.index,
    y = data['Close'],
    name='15 minute average'
))
fig.add_scatter(x=data.index, y=data.Close, name='15 minute average')


fig.update_layout(
    title='Uber live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')


fig.show()