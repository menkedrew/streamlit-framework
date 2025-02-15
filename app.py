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

date_ranges = {'5d': '5 days', '1mo': '1 month','3mo': '3 month', '6mo': '6 month', '1y': '1 year', '2y': '2 year', '5y': '5 year', '10y': '10 year', 'ytd': 'year to date', 'max': 'max date range'}

def prettydate (option):
    return date_ranges.get(option)

selected_date_range = st.selectbox('What date range would you like?: ', date_ranges.keys(), index=0, help="Choose a date range", format_func=prettydate)
st.write('You selected: ', selected_date_range)

df = yf.download(option, group_by="Ticker", period = selected_date_range)

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