import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  #서버에서, 화면에 표시하기 위해 필요 // a non-GUI backend 이래서 화면에 안나옴
import seaborn as sb


def main():
    st.title('Plotting with st.pyplot()')

    df = pd.read_csv('data/iris.csv')
    st.dataframe(df.head(5) )

    fig = plt.figure() # 1. 먼저 차트 영역을 가지고 와서 변수에 저장
    #plt.scatter(data=df, x='sepal_length', y='sepal_width')
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')
    plt.title('length and width')
    st.pyplot(fig)
    # plt.show() #matplotlib.use('Agg')를 했기 때문에 plt.show()가 안됨

    fig2 = plt.figure()
    df['sepal_length'].plot(kind='hist', bins=20) 
    #plt.hist( data= df, x='sepal_length', bins=20) #또는
    plt.xlabel('sepal_length')
    plt.ylabel('value')
    plt.title('length and')
    st.pyplot(fig2)

    #서브 플롯 각각 빈즈 20, 빈즈30개로 , 1행 2열로 만들기
    fig3 = plt.figure()
    plt.subplot(1, 2, 1)
    plt.hist( data= df, x='sepal_length', bins=20)
    plt.subplot(1, 2, 2)
    plt.hist( data= df, x='sepal_length', bins=30) 

    st.pyplot(fig3)


    # species 컬럼의 데이터를, 몇개씩 화면에 보여주세요.
    fig4 = plt.figure()
    sb.countplot(data=df, x='species')
    st.pyplot(fig4)

    # 같은 방법    
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)


if __name__ == '__main__':
    main()
