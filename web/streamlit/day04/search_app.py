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
import re

from df_load_func import df_load 

def run_search():
    # df 가져오기
    df = df_load()

    
    st.dataframe(df)
    st.subheader('가장 연봉이 높은 사람 찾기')
    radio_list = ['연봉 가장 많이 받는 사람', '연봉 가장 적게 받는 사람']
    
    choiceOfUser = st.radio('선택 하세요', radio_list)
    
    if choiceOfUser == radio_list[0]:
        max_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].max() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]
        st.text(max_salary)
    elif choiceOfUser == radio_list[1]:
        min_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].min() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]    
        st.text(min_salary)
    
    st.subheader('고객 검색 하기')
    customerName = st.text_input('입력하세요')
    if customerName:
        if re.match('[a-zA-Z]', customerName) == None:
            st.error('영어 이름만 가능 합니다.')
        else:
            #print(customerName)
            byNameDF = df_load(name = customerName)
            st.dataframe(byNameDF)