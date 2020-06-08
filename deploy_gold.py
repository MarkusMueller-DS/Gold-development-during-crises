import numpy as np
import pandas as pd
import plotly.graph_objects as go

import streamlit as st


# load data
df = pd.read_csv('data/data_plotly_vis.csv')

# create chart
fig = go.Figure()

fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.energy_crisis_1970, mode='lines', name='energy crisis 1970'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.oil_crisis_1973, mode='lines', name='oil crisis 1973'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.early_1980s_recession, mode='lines', name='early 1980s recession'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.black_monday, mode='lines', name='black monday'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.dot_com_bubble, mode='lines', name='dot com_bubble'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.financial_crisis_2007, mode='lines', name='financial crisis_2007'))
fig.add_trace(go.Scatter(x=df.days_in_crisis, y=df.corona_2020, mode='lines', name='corona 2020'))

# change layout
fig.update_layout(title='Gold price development before and during major S&P 500 crashes',
                   xaxis_title='days since first fall',
                   yaxis_title='change in percent')

# sets hovermode to compare data points
fig.layout.hovermode = 'x'

# deploy on streamlit
st.plotly_chart(fig, use_container_width=True)