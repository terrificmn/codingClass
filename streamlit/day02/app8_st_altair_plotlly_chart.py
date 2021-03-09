import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

#참고 사이트 https://altair-viz.github.io


def main():
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)

    lang_list = df1.columns.tolist()
    
    lang_list = lang_list[1 :]  # 'Week'컬럼은 빼기
    
    selected_lang_list = st.multiselect('마음껏 언어를 선택하시오.', lang_list)

    #print(len(selected_lang_list))

    #유저가 선택한 언어만 차트를 그리려고 한다. 
    #필요한 데이터 프레임을 만들어 준다
    if len(selected_lang_list) > 0:  
        #selected_df = df1[selected_lang_list[0: len(selected_lang_list) ]]
        selected_df = df1[selected_lang_list]
        st.line_chart(selected_df)

        st.area_chart(selected_df) #면적으로 음영처리가 됨

    st.write('새로운 영역')

    df2 = pd.read_csv('data/iris.csv')

    st.dataframe(df2.head())

    st.bar_chart( df2[['sepal_length', 'petal_length']] ) 

    # Altair 이용하면, 뭐가 좋냐?
    # x축, y축 설정 + color 또는 size까지 표현 가능

    chart = alt.Chart(df2).mark_circle( opacity=0.9 ).encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species', # legend로 표시 (오른쪽위)
    )
    st.altair_chart(chart, use_container_width=True) #  use_container_width=True 아규먼트는 altair 차트에는 다 사용가능 옆으로 꽉 채워서 보여준다
    
    # 참고 사이트 : 매뉴얼
    # https://altair-viz.github.io/user_guide/marks.html

    df_map = pd.read_csv('data/location.csv')
    st.dataframe(df_map)

    st.map(data = df_map, use_container_width=True)

###############################################################################
############## plotly #########################################################
###############################################################################
    # 참고 plotly 매뉴얼 사이트 https://dash.plotly.com/
    import plotly.express as px

    df4 = pd.read_csv('data/prog_languages_data.csv')
    st.dataframe(df4)

    #plotly의 pie 차트 그리기
    fig1 = px.pie(
                df4, 
                values= 'Sum',
                names = 'lang',
                title = 'Pie Chart of Languages'
            )
    st.plotly_chart(fig1)

    #plotly의 bar 차트 그리기
    fig2 = px.bar(
                df4,
                x = 'lang',
                y = 'Sum'

            )
    st.plotly_chart(fig2)


if __name__ == '__main__':
    main()