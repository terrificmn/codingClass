import streamlit as st

from PIL import Image # 이미지 처리 라이브러리

def main():
    img = Image.open('data/image_03.jpg')
    st.image(img, use_column_width=True) # 이미지 화면에 표시

    st.image('url') # 인터넷 URL을 적어줘도 된다

    video_file = open('data/secret_of_success.mp4', 'rb').read()
    st.video(video_file)

    audio_file = open('data/song.mp3', 'rb').read()
    st.audio(audio_file)

if __name__ == '__main__':
    main()
