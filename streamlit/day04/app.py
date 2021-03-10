import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import h5py
from tensorflow.keras.models import load_model

st.set_page_config(page_title='Car predict', layout='wide', initial_sidebar_state='auto')

# from 첫번째_appif case import 1파일명
# from 두번째_appif case import 2파일명
# from 두번째_appif case import 3파일명
# 예: 
# from eda_app import run_eda_app

def main():
    st.title('EDA')
    st.title('자동차 구매 가격 예측')

    select_list =[
                    '데이터 프레임 보기','검색하기','상관 관계 분석', '예측하기'
        ]
    select_choice = st.sidebar.selectbox('Menu', select_list)
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    df = df.drop(['Customer e-mail', 'Gender'], axis=1)
    
    if select_choice == '데이터 프레임 보기':
        st.dataframe(df)

        # 호출하기
        # 1파일명()    
    # 불러오기
    
        model = load_model('data/model_car')
        #print(model.summary())
    
    elif select_choice == '검색하기':
        #호출하기
        #2파일명()
        st.dataframe(df)
        st.subheader('가장 연봉이 높은 사람 검색하기')
        radio_list = ['연봉 가장 많이 받는 사람', '연봉 가장 적게 받는 사람']
        
        choiceOfUser = st.radio('선택 하세요', radio_list)
        
        if choiceOfUser == radio_list[0]:
            max_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].max() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]
            st.text(max_salary)
        elif choiceOfUser == radio_list[1]:
            min_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].min() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]    
            st.text(min_salary)

    elif select_choice == '상관 관계 분석':
        # sns.pairplot(car_df)
        # plt.show()

        st.subheader('컬럼별로 상관관계 분석')
        radio_list = ['Country', 'Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
        
        selectionOfUser = st.multiselect('선택 하세요', radio_list)
        
        # 선택을 2개 이상할 때 실행 
        selection_nbr = len(selectionOfUser)
        if selection_nbr >= 2:
            if selection_nbr == 2:
                #print(selectionOfUser)
                # 선택한 리스트의 각각 x, y을 저장
                str_x = selectionOfUser[0]
                str_y = selectionOfUser[1]

                fig = plt.figure() 
                sb.regplot(data= df, x = str_x, y = str_y)
                plt.xlabel(str_x)
                plt.ylabel(str_y)
                plt.title(str_x + ' 와 ' + str_y + ' 상관 관계 분석')
                st.pyplot(fig)
            
            # 선택 3개 이상일 경우
            if selection_nbr >= 3 :
                st.subheader(str(selection_nbr) + ' 분석')
                column_list = []
                for column in selectionOfUser:
                    column_list.append(column)

                #print(column_list)
                df_column = df[ column_list ]
                print(column_list)
                
                #pairplot 화면에 안 뿌려짐
                # fig = plt.figure()
                # #sb.pairplot(data = df_column)
                # st.pyplot(fig)
                
                st.text('차트도 보고 가세요!')
                st.dataframe(df_column.corr())
                
        
        elif selection_nbr == 1:
            st.warning('2개 이상 선택을 해주세요')
        # if selectionOfUser == radio_list[0]:
        #     max_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].max() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]
        #     st.text(max_salary)
        # elif selectionOfUser == radio_list[1]:
        #     min_salary = df.loc[ df['Annual Salary'] == df['Annual Salary'].min() , ['Customer Name', 'Country', 'Age', 'Annual Salary']]    
        #     st.text(min_salary)

#새로운 고객 데이터가 있습니다. 이 사람은 차량을 얼마정도 구매 가능한지 예측하시오.
#여자이고, 나이는 38, 연봉은 90000, 카드빚은 2000, 순자산은 500000 일때, 어느정도의 차량을 구매할 수 있을지 예측하시오.
    elif select_choice == '예측하기':
        st.subheader('예측을 하겠습니다.')
        st.radio('성별', ['여자', '남자'])
        st.slider('나이', 10, 100)
        st.text_input('연봉을 입력하세요')
        st.text_input('카드빚을 입력하세요')
        st.text_input('순 자산을 입력하세요')

        if st.button('예측하기'):
            st.warning('아직 만드는 중입니다. ')



if __name__ == '__main__':  
    main() # main() 함수 호출


