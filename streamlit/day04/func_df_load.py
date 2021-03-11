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

from df_load_func import df_load 

def run_df_load():
    # df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    # df = df.drop(['Customer e-mail', 'Gender'], axis=1)
        
    df = df_load()
    st.dataframe(df)

    multi_list = []
    for column in df.columns:
        multi_list.append(column)
        
    selection_col = st.multiselect('보고싶은 컬럼을 선택해 주세요', multi_list)
    selection_len = len(selection_col)

    if selection_len >= 1:
        #print(selection_col)
        
        for column in selection_col:
            selectedDf = df[ selection_col ]
        
        st.dataframe(selectedDf)

    model = load_model('data/car.h5')
    #print(model.summary())

