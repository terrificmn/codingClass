import pandas as pd
import streamlit as st

def transferGender(gender) :
    if gender == 0:
        return 'Woman'
    elif gender == 1:
        return 'Man'
    
def df_load(types='df', **name):
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    #df = df.drop(['Customer e-mail'], axis=1)
    df['Gender'] = df['Gender'].apply(transferGender)
    
    #st.dataframe(df['Gender'].apply(transferGender))

    
    if types == 'float':
        #print( df.dtypes != object )
        # type인 float인 것만 (object가 아닌 것들만 뽑아서 df만들기)
        float_columns = df.columns[ df.dtypes == float ]

        return df[float_columns]
    
    else:
        # 이름 검색이 있을 경우
        if name:
            #print(list(name.values()))
            lowedName = list(name.values())[0].lower()
            lowerdColumn = df['Customer Name'].str.lower().to_frame()
            
            #대소문자 구별 없이 찾는 파라미터 case=False
            df_byName = df.loc[ df['Customer Name'].str.contains(lowedName, case=False) , ]
            return df_byName

        return df

