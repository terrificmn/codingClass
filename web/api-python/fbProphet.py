# 야후 금융에서 주식정보를 제공하는 라이브러리 yfiance 이용
# 주식정보를 불러오고 차트 그리는 것을 합니다.

# 해당 주식에 대한 트윗글들을 불러올 수 있는 api가 있다
# stocktwits.com  에서 제공하는 Restful API 를 호출해서
# 데이터 가져오는 것 실습
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# api로 요청할 수 있는 라이브러리를 설치해줘야한다 
# python requests PyPi
# https://pypi.org/project/requests/
# 설치되어 있다고 하import streamlit as st

# 프로펫 예측을 위해서 라이브러리 설치
# fbprophet이 필요 
# conda install -c conda-forge fbprophet  

from fbprophet import Prophet



def main() :
    st.header('Online Stock Price Ticker')

    # yfinance실행
    symbol = 'MSFT'
    data = yf.Ticker(symbol)

    today = datetime.now().date()
    print(today)

    df = data.history(start='2010-06-01', end=today)

    st.dataframe(df)

    st.subheader('종가')
    
    st.line_chart(df['Close'])

    st.subheader('거래량')

    st.line_chart(df['Volume'])

    # yfinance 라이브러리만의 정보
    #data.info  # (딕셔너리, 리스트로 데이터를 받음)
    #data.calendar
    # data.major_holders
    # data.institutional_holders
    # data.recommendations
    # data.dividends
    div_df = data.dividends

    # (row) 인덱스로 있을 때는 리샘플링 할 수 있다
    st.dataframe(div_df.resample('Y').sum() )

    # 컬럼으로 다시 변환해 준다
    new_df = div_df.reset_index()
    #새로운 컬럼 Year 만들기
    new_df['Year'] = new_df['Date'].dt.year

    st.dataframe(new_df)
    fig = plt.figure()
    plt.bar(new_df['Year'], new_df['Dividends'] )
    st.pyplot(fig)

    # 여러 주식 데이터를 한번에 보여주기
    favorites = ['msft', 'tsla', 'nvda', 'aapl', 'amzn']

    f_df = pd.DataFrame()
    
    # 종가 넣어주기
    for stock in favorites :
        f_df[stock] = yf.Ticker(stock).history(start='2010-01-01', end=today)['Close']
    
    st.dataframe(f_df)
    st.line_chart(f_df)

    # prophet를 사용하기 위해서 컬럼명 바꾸기 
    p_df = df.reset_index()
    p_df.rename(columns = {'Date':'ds', 'Close':'y'}, inplace = True)
    st.dataframe(p_df)

    m = Prophet()
    m.fit(p_df)

    # 1년치로 데이터 프레임 만들기
    future = m.make_future_dataframe(periods=365)

    # 예측하기
    forecast = m.predict(future)

    st.text('예측')
    st.dataframe(forecast)

    fig1 = m.plot(forecast)
    st.pyplot(fig1)

    fig2 = m.plot_components(forecast)
    st.pyplot(fig2)




if __name__ == '__main__' :
    main()
