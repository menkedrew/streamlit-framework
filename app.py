import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file
import yfinance as yf
from bokeh.models import ColumnDataSource
from bokeh.models import DatetimeTickFormatter
from math import pi
from datetime import date

try:
    fp = open('SP500_Tickers.txt')
    sp500 = fp.readlines()
finally:
    fp.close()

option = st.selectbox('Which Ticker would you like to select?: ', sp500, index=0, help="Choose S&P500 Stock tickers",)
st.write('You selected: ', option)

option_sdate = st.selectbox('What date range would you like?: ', ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"], index=0, help="Choose a date range",)
st.write('You selected: ', option_sdate)



df = yf.download(option, group_by="Ticker", period = option_sdate)

st.title(f"Stock Ticker for: {option}")

cds = ColumnDataSource(df)

p = figure(plot_width=800, plot_height=800, title=option, x_axis_label='Time', y_axis_label='Points')

p.outline_line_width = 7
p.outline_line_alpha = 0.3
p.outline_line_color = "red"

p.line(x="Date", y="Close", source=cds, legend_label='Close price: '+ option, line_width=2)

p.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
)
p.xaxis.major_label_orientation = pi/4

p.toolbar.autohide = True

st.bokeh_chart(p, use_container_width=True)