#import
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import h5py
from tensorflow.keras.models import load_model
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import pickle
import joblib

# 주요 함수들 모듈화 임포트 
from func_df_load import run_df_load
from search_app import run_search
from corr_app import show_corr
from ml_app import run_ml_app
from df_load_func import df_load 


st.set_page_config(page_title='Car predict', layout='wide', initial_sidebar_state='auto')

def main():
    st.title('EDA')
    st.title('자동차 구매 가격 예측')

    select_list =[
                    '선택하세요', '데이터 프레임 보기','검색하기','상관 관계 분석', '예측하기'
        ]
    select_choice = st.sidebar.selectbox('Menu', select_list)
    
    
    if select_choice == '선택하세요':
        pass

    if select_choice == '데이터 프레임 보기':
        run_df_load()
    
    elif select_choice == '검색하기':
        run_search()

    elif select_choice == '상관 관계 분석':
        show_corr()

    elif select_choice == '예측하기':
        run_ml_app()
        


if __name__ == '__main__':  
    main() # main() 함수 호출


