import streamlit as st
from PIL import Image
import pandas as pd      
from PyPDF2 import PdfFileReader
import os

# 이미지 처리 로드하는 함수
def load_image(image_file) :
    img = Image.open(image_file)
    return img

# pdf 파일 처리
def read_pdf(pdf_file) :
    pdfReader = PdfFileReader(pdf_file) # pdf_file을 읽을 수 있게 저장
    count = pdfReader.numPages # pdf 페이지 수 반환
    text = '' # 빈문자열 
    for i in range(count):
        page = pdfReader.getPage(i)
        text += page.extractText() # extractText()를 이용해서 페이지의 내용을 텍스트로 풀어준다, 그리고 계속 text에 더해준다
    return text


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
    st.title('파일 업로드 프로젝트')

    menu = ['Image', 'Dataset', 'Documents', 'About']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Image':
        st.subheader('이미지 파일 업로드')
        image_file = st.file_uploader('업로드 이미지', type=['png', 'jpg', 'jpeg']) #type= 에 있는 것만 처리함

        if image_file is not None:
            st.write(type(image_file) ) # 파이썬 형태
            st.write(image_file.name)
            st.write(image_file.size)
            st.write(image_file.type)

            img = load_image(image_file) # upload한 이미지를 load_image():사용자 함수에 넣어줘서 넘겨준다
            st.image(img, width=250 )

            save_uploaded_file('temp', image_file)

    elif choice == 'Dataset':
        st.subheader('CSV 파일 업로드')
        data_file = st.file_uploader('업로드 CSV', type=['csv'])
        if data_file is not None:
            st.write(data_file.name)
            st.write(data_file.type)
            st.write(data_file.size)

            df = pd.read_csv(data_file)
            st.dataframe(df)

            save_uploaded_file('temp', data_file)

    elif choice == 'Documents':
        st.subheader('문서파일 업로드')
        docu_file = st.file_uploader('문서파일 업로드', type=['pdf', 'txt'])
        if docu_file is not None:
            st.write(docu_file.name)
            st.write(docu_file.type)
            st.write(docu_file.size)

            if st.button('확인'):
                st.write('버튼 클릭 되었습니다')
                # st.write(docu_file.type) # type확인용

                # pdf 파일 일때 처리
                if docu_file.type == 'application/pdf':
                    # pdf파일을 처리하려면 pdf 라이브러리 필요함
                    # PyPDF2 를 설치해야함 
                    # https://pypi.org/project/PyPDF2/ 에서 검색한 후 컨매드 복사 후 터미널에 실행
                    # 바로 터미널에 실행하려면 pip install PyPDF2
                    # (streamlit) 가상환경인지 확인 후 실행
                    text = read_pdf(docu_file) # 사용자 함수 호출
                    st.write(text)
                    save_uploaded_file('temp', docu_file)

                elif docu_file.type == 'text/plain':
                    text = str(docu_file.read(), 'utf-8') # str로 바꾸기
                    st.write(text)
                    save_uploaded_file('temp', docu_file)

                else:
                    st.error('PDF, TXT가 아닌 파일은 업로드 불가')


    elif choice == 'About':
        pass




if __name__ == '__main__':
    main()

