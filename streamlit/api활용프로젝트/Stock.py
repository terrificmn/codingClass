import streamlit as st
import re
import requests

class StockController :
        
    def validation(self, symbol):
        regex = '^[a-zA-Z0-9]+$'
        
        # 공백 제거
        symbol = symbol.strip(' ')
        
        if len(symbol) == 0 :
            st.error('입력해주세요')
            return False

        elif not re.search(regex, symbol) :
            st.error('검색은 영문만 지원합니다.')
            return False

        else :
            # 마지막 최종적으로 통과시에 True 리턴
            return True
    
    def st_twits(self, symbol, isSymbol = True) :
        

        if isSymbol == False :
            com = symbol  # 헛깔리니깐 변수명 바꾸기 
            res = requests.get('https://api.stocktwits.com/api/2/streams/user/170.json')
            res_data = res.json()
            st.write(res_data)

        # symbol로 검색할 시
        else : # 기본값 True일때 symbol로 검색    
            res = requests.get('https://api.stocktwits.com/api/2/streams/symbol/{}.json'.format(symbol))
            res_data = res.json()    
            
            if res_data['response']['status'] != 200 : 
                st.error('티커가 없거나 잘못 입력하셨습니다.')
            else :
            #st.write(res_data)

                # json()메소드로 json형식이므로 응답받은 res 를 변환해서 저장
                st.write(res_data['symbol']['title'] + ' Stock 정보 입니다.')
                st.markdown('___')

                for message in res_data['messages'] :
                    #st.write(message)
                    # beta_columns() 는 컬럼을 비율을 설정해줌 
                    # (컬럼요소가 2개를 썼으므로 2개이고 왼쪽 비율이 1 오른쪽컬럼 비율이 4)
                    # 그리고 col 변수에 저장해서 with col1, col2, ... 과 같이 해서 사용
                    col1, col2 = st.beta_columns( [2, 6])
                    st.markdown('___')
                    with col1 :
                        st.image( message['user']['avatar_url'] )
                        st.write( message['user']['username'] )
                    with col2 :
                        st.write( message['body'] ) 
                        st.write( '올린 시간: ' + message['created_at'] )
                        st.write( '좋아요👍 :' + str(message['user']['like_count']) )