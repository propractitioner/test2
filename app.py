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
        try:
            stock = yf.Ticker(ticker)
            market_cap = stock.info['marketCap']
            if market_cap:
                market_caps[ticker] = market_cap
            else:
                st.warning(f'{ticker}의 시가 총액 정보를 가져올 수 없습니다.')
        except Exception as e:
            st.error(f'{ticker}의 데이터를 가져오는 중 오류가 발생했습니다: {e}')
    return market_caps

if tickers:
    tickers = [ticker.strip().upper() for ticker in tickers.split(',')]
    market_caps = get_market_caps(tickers)

    # 시가 총액 시각화
    if market_caps:
        fig, ax = plt.subplots()
        sizes = [market_caps[ticker] for ticker in tickers if ticker in market_caps]
        labels = [ticker for ticker in tickers if ticker in market_caps]

        # 원의 위치를 랜덤하게 생성
        x = range(len(sizes))
        y = [1] * len(sizes)
        
        ax.scatter(x, y, s=[size / 1e9 for size in sizes], alpha=0.5)
        
        # 라벨 추가
        for i, label in enumerate(labels):
            ax.text(x[i], y[i], label, horizontalalignment='center', verticalalignment='center')

        plt.axis('off')
        st.pyplot(fig)
    else:
        st.info('유효한 티커를 입력하세요.')
else:
    st.info('주식 티커를 입력하세요.')
