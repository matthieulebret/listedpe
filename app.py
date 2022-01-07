
# import plotly.express as px
# import plotly.graph_objs as go

import altair as alt
# import time
# import requests

import numpy as np
import pandas as pd
import datetime
import calendar

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import xlrd
import lxml

import yfinance as yf
import streamlit as st

st.set_page_config('Stock market analysis',layout='wide')

st.title('Stock market analysis')





### Triggers

st.header('Stock prices')


# s = yf.Ticker('RDSB.L')
# ca = yf.Ticker('ACA.PA')
# inf = yf.Ticker('IFX.DE')
# daim = yf.Ticker('DAI.DE')
#
#
# tickers = [s,ca,inf,daim]
#
# prices = []
# for ticker in tickers:
#     try:
#         pricelist = ticker.history(start='2021-07-06',prepost=True)['Close']
#         prices.append(pricelist)
#
#     except:
#         prices.append(0)
#
#
# dailyclose = pd.DataFrame(prices).transpose()


dailyclose = yf.download('OCI.L BPT.L PIN.L ^FTSE',start = '2021-07-22')['Close']

dailyclose

st.header('Performance')


perf = dailyclose / dailyclose.iloc[0,:] -1
perf

st.line_chart(perf)

st.header('Correlations')

correl = perf.corr()
correl

st.stop()
