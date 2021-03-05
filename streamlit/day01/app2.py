import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data/iris.csv')
    
    # st.dataframe( df )
    # st.dataframe( df.style.highlight_max(axis = 0) ) # 컬럼별 max값을 하이라이트

    #st.table(df)  # 스태틱한 방법, 자체 스크롤이 없다 (작은창으로 표시되지 않고 전체 표시)
    #st.table(df.head() )  # head()를 이용해서 기본 5개 보여줌

    #st.write( df.head() )


if __name__ == '__main__':
    main()


print('heelo')