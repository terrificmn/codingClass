import streamlit as st
import pandas as pd

def main():
    # if st.button('데이터 보기'):
    #     st.write('데이터 프레임.')
    #     df = pd.read_csv('data/iris.csv')
    #     st.dataframe(df)

    # name = '홍길동'
    # if st.button('이름확인'):
    #     st.write('당신의ㅡ 이름은 {} 입니다.'.format(name))

    # if st.button('이름확인', key='btn2'):  #button메소드에서 표시되는 내용이 같은 경우는 안됨
    # # key='btn2' 식으로 key 저장을 해준다
    #     st.write('안녕하세요')

    # name = 'Jessy'
    # if st.button('이름확인'):
    #     st.write( name.upper())

    # if st.button('이름확인', key='btn2'):  #button메소드에서 표시되는 내용이 같은 경우는 안됨
    #     st.write( name.lower())

    #라디오 버튼을 누르게 되면 변수에 저장 (리스트 첫번째, 두번째)
    status = st.radio('정렬을 선택하세요', (['오름차순', '내림차순']))

    # 라디오 버튼 만들기
    # df = pd.read_csv('data/iris.csv')
    # if status == '오름차순':
    #     st.write('오름차순 눌렀어요.')
    #     st.dataframe(df.sort_values(by='sepal_length', ascending=True))
    # elif status == '내림차순':
    #     st.write('내림차순 눌렀어요.')
    #     st.dataframe(df.sort_values(by='sepal_length', ascending=False))


    # 체크 박스 만들기 checkbox()메소드, selectbox()메소드
    if st.checkbox('show / hide'): #체크박스가 눌리면 if문 실행
        st.text('뭔가 하겠다.')

    lang = ['Python', 'Java', 'C', 'Go']

    selected_lang = st.selectbox("언어 선택하세요", lang)
    #st.write(selected_lang )

    st.write('당신이 선택한 언어는 {} 입니다.'.format(selected_lang))
    

    lang_list = st.multiselect( '언어를 선택하세요', lang)
    #print(lang_list) #터미널에 표시되므로 디버깅 할때나 확인할 때 주로 사용

    age = st.slider('나이', 1, 100)
    print(age)
    st.write('당신이 선택한 나이는 {} 입니다.'.format(age))

if __name__ == '__main__':
    main()