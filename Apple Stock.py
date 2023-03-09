import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Котировки акций компании Apple",
    page_icon="🍏")

st.write("""
# Веб-приложение для просмотра данных о котировках акций компании Apple

Ниже приведены данные о **минимальных** и **максимальных** ценах акций, а также об **объёме** торгов.

""")

st.sidebar.header('Выберите период')

start_date = date(2010, 1, 1)
end_date = date(2023, 3, 1)


def user_input_features():
    highest_price_date = st.sidebar.slider('Период для отображения максимальной цены', start_date, end_date,
                                           value=(date(2014, 1, 1), date(2020, 1, 1)))
    lowest_price_date = st.sidebar.slider('Период для отображения минимальной цены', start_date, end_date,
                                          value=(date(2014, 1, 1), date(2020, 1, 1)))
    volume_date = st.sidebar.slider('Период для отображения объёма торгов', start_date, end_date,
                                    value=(date(2014, 1, 1), date(2020, 1, 1)))
    data = {'Период для отображения максимальной цены': highest_price_date,
            'Период для отображения минимальной цены': lowest_price_date,
            'Период для отображения объёма торгов': volume_date}
    features = pd.DataFrame(data)
    return features


df = user_input_features()

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf_max = tickerData.history(period='1d', start=df['Период для отображения максимальной цены'].loc[df.index[0]],
                                  end=df['Период для отображения максимальной цены'].loc[df.index[1]])
tickerDf_min = tickerData.history(period='1d', start=df['Период для отображения минимальной цены'].loc[df.index[0]],
                                  end=df['Период для отображения минимальной цены'].loc[df.index[1]])
tickerDf_vol = tickerData.history(period='1d', start=df['Период для отображения объёма торгов'].loc[df.index[0]],
                                  end=df['Период для отображения объёма торгов'].loc[df.index[1]])

st.write("""
### Максимальная цена акций
""")
st.line_chart(tickerDf_max.High, )

st.write("""
### Минимальная цена акций
""")
st.line_chart(tickerDf_min.Low)

st.write("""
### Объём торгов
""")
st.line_chart(tickerDf_vol.Volume)
