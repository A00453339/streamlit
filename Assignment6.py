import streamlit as st
import pandas as pd
import requests as rq
import plotly.express as px

st.header('Bitcoin Prices')
num_of_days=st.slider('No. of days',1,365,10)
#st.write(num_of_days)

currency=st.radio('Currency',('cad','usd','inr'),0)
url='https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency='+str(currency)+'&days='+str(num_of_days)+'&interval=daily'
data = rq.get(url)
lol = data.json()['prices']
df = pd.DataFrame(lol,columns=['date','price'])
df['date']=pd.to_datetime(df['date'],unit='ms')

fig = px.line(df,x='date',y='price')
st.plotly_chart(fig)

st.write('Average price during this time was ' + str((df['price'].sum())/num_of_days))

