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

# joblib 을 이용해서 저장하기 (스케일러 저장하기)
#joblib.dump(mmX, 'mmX.pkl')

# 충돌 일어날때 가상환경에서 업그레이드 해주기
# pip install scikit-learn-0.23.2 

# 예측 본론

# 학습 => 오차를 줄이는 것
# validataion은 에포크 끝난 (학습 1회 끝남) 문제를 주고, 계산만 함
# 정답을 알려주지 않음, 

# 예제 데이터
#새로운 고객 데이터가 있습니다. 이 사람은 차량을 얼마정도 구매 가능한지 예측하시오.
#여자이고, 나이는 38, 연봉은 90000, 카드빚은 2000, 순자산은 500000 일때, 어느정도의 차량을 구매할 수 있을지 예측하시오.
def run_ml_app():

    st.subheader('Machine Learning')

    # 파일명.h5 저장한 것을 불러오기
    model = tensorflow.keras.models.load_model('data/car.h5')
    
    st.text('예시 데이터, 만약 여자이고, 나이가 38, 연봉 90000, 카드빚은 2000, 순자산 500000 일 때 어느정도의 차량을 구매할 수 있을까?')
    new_data = np.array( [ 0, 38, 90000, 2000, 500000 ] )
    # feature scaling을 하기 위해 2차원으로 만들어 준다
    new_data = new_data.reshape(1, -1)

    ## mm_X 객체 불러오기
    mm_X = joblib.load('data/mm_X.pkl')

    # Feature Scaling 하기
    # 기존 객체를 사용하기 때문에 transform()으로 함
    # 새로운 데이터를 mm_X 객체를 이용해서 피쳐스케일링
    new_data = mm_X.transform(new_data)

    #예측
    new_y_pred = model.predict(new_data)

    #출력하기
    st.write( new_y_pred[0][0])
    
    # mm_y 객체 불러오기, 결과값을 돌려주기 위해서 필요
    mm_y = joblib.load('data/mm_y.pkl')
    
    # 새로운 데이터 예측결과를 원래 값으로 돌려주기
    # 새롭게 받은 데이터로 예측을 한 다음에 이것을 다시 원래 (피쳐스케일링 되기 전의 값)값으로 돌려주기 위해서 
    # 필요
    new_y_pred_original = mm_y.inverse_transform(new_y_pred)

    #화면 표시
    st.write( new_y_pred_original )


    st.subheader('당신의 데이터를 입력하세요.자동차 구매 가격을 예측해드립니다.')
    gender = st.radio('성별', ['여자', '남자'])
    if gender == '여자':
        gender = 0
    else:
        gender = 1

    age = st.slider('나이', 10, 100)

    salary = st.number_input('연봉을 입력하세요', min_value=0)
    debt = st.number_input('카드빚을 입력하세요', min_value=0)
    worth = st.number_input('순 자산을 입력하세요', min_value=0)

    if st.button('예측하기'):
        st.warning('아직 만드는 중입니다. ')

        user_data = np.array( [ gender, age, salary, debt, worth ] )

        #피쳐스 스케일링
        user_data = user_data.reshape(1, -1)
        mm_X = joblib.load('data/mm_X.pkl')

        user_data = mm_X.transform(user_data)

        #예측하기
        y_pred = model.predict(user_data)

        #에측 결과는 스케일링 된 결과이므로, 다시 돌려야 한다
        # 스켈일러 (객체) 불러오기
        mm_y = joblib.load('data/mm_y.pkl')

        #원래로 돌리기 
        y_pred_original = mm_y.inverse_transform(y_pred)

        # 결과 화면 출력
        st.write('예측 결과 입니다. 당신은 %.0f 달러 정도의 자동차를 구매할 수 있습니다.' % y_pred_original[0, 0] )
        