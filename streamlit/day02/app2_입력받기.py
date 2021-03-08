import streamlit as st

def main():
    fname = st.text_input('이름을 입력하세요!')
    st.title(fname)

    fname2 = st.text_input('이름을 입력하세요!', max_chars=5)
    st.text(fname2)

    # 여러줄 입력 받기
    message = st.text_area('메세지를 입력하세요.', height=3)
    st.write(message)

    number = st.number_input('숫자 입력', 1, 100) # 숫자 제한하기 (1~100) , 기본은 실수로 나옴
    st.write(number)

    number2 = st.number_input('숫자 입력', 1.0, 10.0) # 실수 숫자 제한하기 
    st.write(number2)

    my_date = st.date_input('약속 날짜')
    st.write(my_date)

    my_time = st.time_input('시간 선택')
    st.write(my_time)

    password = st.text_input('비밀번호 입력하세요', type='password', max_chars=12)
    st.write(password)

    color = st.color_picker('색을 선택하세요.')
    st.write(color) #16진수로 r g b 값을 보여준다


if __name__ == '__main__':
    main()

