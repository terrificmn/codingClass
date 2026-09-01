import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader('EDA 화면 입니다.')
    st.write('다른 파일에서 불러옴')
    
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)


