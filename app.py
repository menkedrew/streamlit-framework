import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
from bokeh.plotting import figure, show
import yfinance as yf
from bokeh.models import ColumnDataSource
from bokeh.models import DatetimeTickFormatter
from math import pi

df = yf.download("MSFT", start="2021-12-01", end="2021-12-31", group_by="Ticker")

st.title("Stock Ticker")

cds = ColumnDataSource(df)

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x="Date", y="Close", source=cds, legend_label='Trend', line_width=2)

p.xaxis.formatter=DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
)
p.xaxis.major_label_orientation = pi/4

st.bokeh_chart(p, use_container_width=True)