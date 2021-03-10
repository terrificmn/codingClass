from modules import import_modules

def show_corr():
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