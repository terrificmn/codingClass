import streamlit as st 
from PIL import Image, ImageFilter, ImageEnhance
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
    
    return st.success('{} 파일 업로드가 완료 되었습니다.'.format(file.name) )
    


def main():
    img = Image.open('data/birds.jpg')
    #st.image(img)

    option_list = ['Show Image', 'Rotate Image', 'Create Thumbnail', 
                    'Crop Image', 'Merge Images', 'Flip Image', 
                    'Black & White', 'Filters - Sharpen', 'Filters - Edge Enhance',
                    'Contrast Image']
    ### 참고:
    ## 썸네일 같은 경우는 서버에 업로드 할 때 같은 이미지를 사이즈별로 만들어 둔다고 한다
    # 그래야 네트워크에서 원할하게 서비스가 될 수 있음
    option = st.selectbox('옵션을 선택하세요.', option_list)
    

    if option == 'Show Image':
        st.image(img)

    elif option == 'Rotate Image':
        rotated_img = img.rotate(90)
        st.image(rotated_img)

    elif option == 'Create Thumbnail':
        size = (200, 200)  #size을 튜플로 지정해줌
        img.thumbnail(size) 
        img.save('data/thumb.png')  # 이미지 저장
        st.image(img)

    elif option == 'Crop Image':
        # 왼쪽 윗부분 부터 시작해서, 너비와 깊이 만큼 잘라라
        # 왼쪽 위부분 좌표 (50, 100) -- 처음 좌표 설정이 됨
        # 너비 x축으로, 깊이 y축으로 (200, 200)
        box = (50, 100, 200, 200)
        cropped_img = img.crop(box)
        cropped_img.save('data/crop.png')
        st.image(cropped_img)

    elif option == 'Merge Images':
        # file_uploader를 또 사용하면 key= 파라미터를 다른이름을 써줘야한다 예; key='merge'
        merge_file = st.file_uploader('Upload Image', type=['png', 'jpeg', 'jpg'], key='merge')
        
        if merge_file is not None:
            merge_img = load_image(merge_file)

            start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1)
            start_y = st.number_input('시작 y 좌표', 0, img.size[0]-1)
            
            position = (start_x, start_y)
            img.paste(merge_img, position) #img 위에 합쳐서
            st.image(img) #img를 표시한다

    elif option == 'Flip Image':
        flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT)
        st.image(flipped_img)
        st.image(img)

    elif option == 'Black & White':
        bw = img.convert('1') # 1 이 black and white 임
        # bw = img.convert('RGB') # 1 이 black and white 임
        st.image(bw)

    elif option == 'Filters - Sharpen':
        sharp_img = img.filter(ImageFilter.SHARPEN)
        st.image(sharp_img)

    elif option == 'Filters - Edge Enhance':
        edged_img = img.filter(ImageFilter.EDGE_ENHANCE)
        st.image(edged_img)


    elif option == 'Contrast Image':
        contrast_img = ImageEnhance.Contrast(img).enhance(2)
        st.image(contrast_img)




#######################################################################
#######################################################################
#######################################################################

# 1. 이미지를 내가 마음대로 올리 수 있어야 한다.
    # 1장만 업로드

# 2. 하드코딩된 코드를, 유저한테 입력 받아서 처리할 수 있도록 바꾼다
    # rotation 할 수 있게 입력 받기 만든 후 rotate 시켜주기
    # thumbnail 사이즈 입력 받기
    # crop 사이즈 받기
    # flip도 종류 선택할 수 있게 하기
    # 블랙 / white/ rgb로 선택할 수 있게 하기 (옵션)

    
    #load_image()
    upload_img = st.file_uploader('이미지 파일을 업로드 하세요.', type=['png', 'jpeg', 'jpg'])
    

    if upload_img is not None:
        save_uploaded_file('temp', upload_img)
        img = load_image(upload_img)

        user_option_list = ['선택하세요.', 'Rotate Image', 'Create Thumbnail', 'Crop Image', 'Flip Image', 'Color Change']
        user_option = st.selectbox('옵션을 선택하세요.', user_option_list)
        
        if user_option == '선택하세요':
            pass

        elif user_option == 'Rotate Image':
            user_rotate = st.text_input('회전을 입력하세요!', max_chars=5)
            print(user_rotate)
            
            if user_rotate != "":
                rotated_img = img.rotate(int(user_rotate))
                st.image(rotated_img)
                #st.write('hello')
                #print(type(user_rotate))

        elif user_option == 'Create Thumbnail':
            user_thunbnail_row = st.text_input('원하는 가로 크기를 입력하세요.', max_chars=3)
            user_thunbnail_col = st.text_input('원하는 세로 크기를 입력하세요.', max_chars=3)
            
            if (user_thunbnail_row != "") and (user_thunbnail_col != "") :

                size = (int(user_thunbnail_row), int(user_thunbnail_col))  #size을 튜플로 지정해줌
                img.thumbnail(size) 
                img.save('temp/thumb.png')  # 이미지 저장
                st.image(img)

        elif user_option == 'Crop Image':
            user_crop_left_top = st.slider('시작하는 부분의 왼쪽상단위치를 선택하세요', 1, 100)
            user_crop_right_top = st.slider('시작하는 부분의 상단오른쪽 위치를 선택하세요', 1, 100)
            # int로 변환 후 저장
            user_crop_left_top, user_crop_right_top = int(user_crop_left_top), int(user_crop_right_top)
            xy = st.text_input('원하는 사이즈를 입력하세요. 입력 예: 100-200')
            max_width = img.size[0] - user_crop_left_top
            max_height = img.size[1] - user_crop_right_top
            #print(max_width)
            #print(max_height)
            if xy != "":
                xy_splited = xy.split('-')
                xy_len = len(xy_splited)
                
                print(xy_len)
                
                if xy_len == 0 or xy_len == 1 :
                    st.warning('사이즈를 입력하세요.')
                elif  xy_len > 2:
                    st.warning('두 개 이상 입력하셨습니다.')  
                else:
                    x, y = int(xy_splited[0]), int(xy_splited[1])
                    
                    box = (user_crop_left_top, user_crop_right_top, x, y)
                    cropped_img = img.crop(box)
                    cropped_img.save('data/crop.png')
                    st.image(cropped_img)

        elif user_option == 'Flip Image':
            status = st.radio('플립 선택', ['수직(위/아래)로 뒤집기', '수평으로(왼쪽/오른쪽) 뒤집기'] )
            
            if status == '수직(위/아래)로 뒤집기':
                flipped_img = img.transpose( Image.FLIP_TOP_BOTTOM)
                st.image(flipped_img)
            else:
                flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT)
                st.image(flipped_img)
        
        elif user_option == 'Color Change':
            color_list = ['Color', 'Gray', 'Black&White']

            status = st.radio( '바꾸고 싶은 색을 선택해 주세요', color_list)

            if status == 'Color':
                bw = img.convert('RGB') 
                
            elif status == 'Gray':
                bw = img.convert('L')
                
            else :
                bw = img.convert('1')

            

            if bw is not None:
                st.image(bw)
                
                
            

        #선생님 코드
        # start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1)
        # start_y = st.number_input('시작 y 좌표', 0, img.size[0]-1)
        # max_width = img.size[0] - start_x
        # max_height = img.size[1] - start_y
        #width = st.number_input('width 입력', 1, max_width)
        #height = st.number_input('height 입력', 1, max_height)
        #box = (start_x, start_y, start_x+width, start_y+height)
        #나머지는 크랍코드

    

if __name__ == '__main__':
    main()

