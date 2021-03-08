import streamlit as st
from PIL import Image
import pandas as pd
import os


# 이미지 처리 로드하는 함수
def load_image(image_file) :
    img = Image.open(image_file)
    return img

# 디렉토리와 파일을 주면, 해당 디렉토리에 이 파일을 저장하는 함수
def save_uploaded_file(directory, file):
    # 1. 디렉토리가 있는지 확인, 없으면 만든다
    if not os.path.exists(directory):
        os.makedirs(directory) # 없으면 만듬

    # 2. 디렉토리가 있으니깐 파일을 저장    
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer() )
    
    return st.success('Successfully saved file: {} in {}'.format(file.name, directory) )


def main():
    st.title('여러 파일들을 업로드하는 앱')
    
    # 사이드바용 메뉴
    menu = ['Home', 'Dataset', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        uploaded_files = st.file_uploader('이미지 파일을 업로드 하세요.', type=['png', 'jpeg', 'jpg'], accept_multiple_files=True)

        if uploaded_files is not None:
            st.write(uploaded_files) # 화면에 출력해주는데 이미지를 표시하는 것이 아니고 리스트 상태를 보여줌

            for img_file in uploaded_files:
                save_uploaded_file('temp', img_file)
                
                img = load_image(img_file)
                st.image(img)


    elif choice == 'Dataset':
        uploaded_files = st.file_uploader('csv파일을 업로드 하세요.', type='csv', accept_multiple_files=True)
            
        if uploaded_files is not None:
            st.write(uploaded_files) # 화면에 출력해주는데 이미지를 표시하는 것이 아니고 리스트 상태를 보여줌
    
        uploaded_file_list = []
        for csv_file in uploaded_files:
            save_confirmed = save_uploaded_file('temp', csv_file)
            uploaded_file_list.append(csv_file.name)
        
        
        # 파일저장이 모두 끝나면, 화면에 셀렉트박스 보여주고 
        # 올린 csv 파일을 선택하면
        # 데이터프레임이 나오도록 코드 작성    
        # 위의 코드에 unploaded_file_list = [] 추가 했고, csv_file이 반복할 때 이름을 리스트에 넣어줌
            
        if len(uploaded_file_list) != 0:
            st.write(uploaded_file_list)
            selected_csv_file = st.selectbox('업로드 한 파일 중 원하는 파일을 선택해주세요', uploaded_file_list)
            
            st.dataframe(pd.read_csv('temp/'+ selected_csv_file))


if __name__ == '__main__':
    main()
