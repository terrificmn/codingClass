import streamlit as st
import requests
import time
import pandas
from Stock import StockController
st.set_page_config(page_title='Stocktwits App', page_icon=None, layout='centered', initial_sidebar_state='auto')

def main() :
    
    selectbox = st.sidebar.selectbox("주식 트윗 보기", ['코멘트 검색하기', ])
    
    st.title('궁금한 주식 티커를 입력해 보세요~')
    symbol = st.text_input('티커 입력: ')

    Stock = StockController()

    if st.button('입력') :
        if Stock.validation(symbol) : #validation 통과면 true 리턴
            Stock.st_twits(symbol)

    st.markdown('<br><br>', unsafe_allow_html=True)
    
    
    # 회사 이름은 더 검색해 봐야할 듯 ..;;
    #com = st.text_input('회사 이름으로 검색: ')
    # if st.button('확인') :
    #     if Stock.validation(com) :
    #         Stock.st_twits(com, False)

    # 프로그레스 바
    # my_bar = st.progress(0)
    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)

    #st.balloons()

    #text로 시간 표시하기
    # with st.empty():
    #     for seconds in range(5):
    #         st.write(f"⏳ {seconds} seconds have passed")
    #         time.sleep(1)
    #         st.write("✔️ 1 minute over!")



if __name__ == '__main__' :
    main()