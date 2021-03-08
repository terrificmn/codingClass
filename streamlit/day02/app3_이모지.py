import streamlit as st
from PIL import Image

# https://emojipedia.org/  #이모티콘 검색 사이트
# page_icon= 이모지를 넣어주면 됨, 그러면 타이틀에 이모지 아이콘이 들어감
# 또는 jpg파일을 직접 넣어줄 수도 있음

img = Image.open('data/image_03.jpg')
st.set_page_config(page_title='스트림릿 Machine Learning', page_icon =img, layout='wide', initial_sidebar_state='collapsed')
# initial_sidebar_state=은 자동으로 auto가 기본 (auto화면 크기에 따라서 다름)
# initial_sidebar_state='collapsed'는 메뉴가 접혀있음


def main():
    st.title('money~ 🤑')
    st.sidebar.success('Menu')


if __name__ == '__main__':
    main()

