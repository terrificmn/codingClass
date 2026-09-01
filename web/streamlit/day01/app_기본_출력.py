## 대개 실무에서 시작파일 이름이 app.py 로 시작하면 main 페이지라고 보면 됨

# 터미널에서 파일이 있는 경로로 이동 후 
# streamlit run app.py 입력하면 시작됨

import streamlit as st

def main():
    st.title('Hello World!')

    name = '김나나'
    st.text('안녕하세요. 저는 {}입니다.'.format(name) )

    st.header('안녕하세요')
    st.subheader('안녕하세요')

    st.markdown('# 큰글자(h1)')
    st.markdown('## 그다음클글자(h2)')

    st.success('성공했을 때: 성공했습니다!')  #녹색화면으로 뜸
    st.warning('경고를 하고 싶을 때')
    st.info('인포를 주고 싶을 때')
    st.error('에러가 발생했습니다.') 
    st.exception('예외 상황이 발생했을 때')  # try catch 구문으로 해야함
    

# 파일 모듈을 인터프리터에서 실행했을 때 즉, import를 한 경우가 아니라면
# 현재 이 파일이 '__main__'이 되고 
# __name__ 이란 글로벌 변수에 저장이 되어서 실행되게 됨
if __name__ == '__main__':  
    main() # main() 함수 호출
