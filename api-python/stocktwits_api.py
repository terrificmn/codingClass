#참고 :https://api.stocktwits.com/developers/docs/api#streams-symbol-docs

#URL 부분을 보면 restful api url이 나오는데 
#이것을 만들 수 있는 것이 목표

# 함수 호출하듯이 api도 호출을 하는데 
# 사용예
# curl -X GET https://api.stocktwits.com/api/2/streams/symbol/AAPL.json
# 심볼만 (티커)만 바꿔서 요청하면 된다. (AAPL.json, MSFT.json ....)



import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

# API 호출을 위한 라이브러리 임포트
import requests


def main() :
    symbol = st.text_input('심볼을 입력하세요')

    if len(symbol) > 0 :
        # 스탁트윗의 API를 호출 30개를 보내줌
        # AAPL.json 의 티커만 바꿔주면 됨
        #res = requests.get('https://api.stocktwits.com/api/2/streams/symbol/AAPL.json')
        res = requests.get('https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol))
        
        # json()메소드로 json형식이므로 응답받은 res 를 변환해서 저장
        res_data = res.json()

        # 파이썬의 딕셔너리와 리스트의 조합으로 사용
        #st.write(res_data) # json데이터 전체 표시

        for message in res_data['messages'] :
            #st.write(message)
            # beta_columns() 는 컬럼을 비율을 설정해줌 
            # (컬럼요소가 2개를 썼으므로 2개이고 왼쪽 비율이 1 오른쪽컬럼 비율이 4)
            # 그리고 col 변수에 저장해서 with col1, col2, ... 과 같이 해서 사용
            col1, col2 = st.beta_columns( [1, 4])

            with col1 :
                st.image( message['user']['avatar_url'] )
            with col2 :
                st.write( '유저 이름:' + message['user']['username'] )
                st.write( '트윗 내용:' + message['body'] )
                st.write( '올린 시간:' + message['created_at'] )
    


if __name__ == '__main__' :
    main()


