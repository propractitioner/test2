import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Streamlit 앱 설정
st.title('주식 시가 총액 크기 비교')

# 사용자 입력 받기
tickers = st.text_input('주식 티커를 콤마로 구분하여 입력하세요', 'AAPL,MSFT,GOOGL,AMZN,TSLA')

# 주식 데이터를 가져오고 시가 총액 계산
def get_market_caps(tickers):
    market_caps = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        market_cap = stock.info['marketCap']
        market_caps[ticker] = market_cap
    return market_caps

if tickers:
    tickers = [ticker.strip() for ticker in tickers.split(',')]
    market_caps = get_market_caps(tickers)

    # 시가 총액 시각화
    if market_caps:
        fig, ax = plt.subplots()
        sizes = [market_caps[ticker] for ticker in tickers]
        labels = [f"{ticker}\n${market_caps[ticker]:.2e}" for ticker in tickers]
        
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig)
