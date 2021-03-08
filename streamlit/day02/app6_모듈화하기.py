import streamlit as st
from eda_app import run_eda_app   # 파일단위로 모듈로 관리하기 / 파일안에서는 함수로 만든다
from ml_app import run_ml_app

def main():
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML', 'About'] #EDA 데이터분석, ML machine learning
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('홈 화면 입니다.')

    elif choice == 'EDA':
        run_eda_app()
    
    elif choice == 'ML':
        run_ml_app()

    else :
        st.subheader('프로젝트 소개 화면 입니다.')











if __name__ == '__main__' :
    main()

