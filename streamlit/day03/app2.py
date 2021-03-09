import streamlit as st 
from PIL import Image, ImageFilter, ImageEnhance
import os
from datetime import datetime
import random

# 이미지 처리 로드하는 함수
def load_image(image_file) :
    img = Image.open(image_file)
    return img

# 디렉토리와 파일을 주면, 해당 디렉토리에 이미지 파일을 저장하는 함수
def save_uploaded_file(directory, img):
    # 1. 디렉토리가 있는지 확인, 없으면 만든다
    if not os.path.exists(directory):
        os.makedirs(directory) # 없으면 만듬

    # 2. 이미지 저장 img.save()
    # datetime.now()을 이용해서 isoformat()으로 바꿔주기
    # : .은 에러가 남 ----> replace로 바꿔준다
    isoNowTime = str(datetime.now().isoformat()).replace(':', '-').replace('.', '-')
    # 2개 정도는 마이크로 시간 이후로 같아서 랜덤으로 만들어 주기
    random_nbr = '-'+ str(random.randint(1,10)) 
    filename_exe = isoNowTime+random_nbr+'.jpg'
    #print(filename_exe)
    img.save(directory + '/' + filename_exe )

    return st.success('{}이 {}에 파일이 저장 되었습니다.'.format(filename_exe, directory) )
    


def main():
#     

#     elif option == 'Filters - Sharpen':
#         sharp_img = img.filter(ImageFilter.SHARPEN)
#         st.image(sharp_img)

#     elif option == 'Filters - Edge Enhance':
#         edged_img = img.filter(ImageFilter.EDGE_ENHANCE)
#         st.image(edged_img)


#     elif option == 'Contrast Image':
#         contrast_img = ImageEnhance.Contrast(img).enhance(2)
#         st.image(contrast_img)




# #######################################################################
# #######################################################################
# #######################################################################

# # 1. 이미지를 내가 마음대로 올리 수 있어야 한다.
#     # 1장만 업로드

# # 2. 하드코딩된 코드를, 유저한테 입력 받아서 처리할 수 있도록 바꾼다
#     # rotation 할 수 있게 입력 받기 만든 후 rotate 시켜주기
#     # thumbnail 사이즈 입력 받기
#     # crop 사이즈 받기
#     # flip도 종류 선택할 수 있게 하기
#     # 블랙 / white/ rgb로 선택할 수 있게 하기 (옵션)

    
    
    upload_img_list = st.file_uploader('이미지 파일을 업로드 하세요.', type=['png', 'jpeg', 'jpg'], accept_multiple_files=True)
    
    if upload_img_list is not None:
        #print(upload_img_list)

        # 2-1 각 파일을 이미지로 바꿔줘야 한다.
        image_list = []
        # 2-2 모든 파일이 image_list에 이미지로 저장됨
        for image_file in upload_img_list:
            img = load_image(image_file)
            image_list.append(img)

        # 3. 이미지 화면에 출력
        # for img in image_list:
        #     st.image(img)


        user_option = ['선택하세요.', 'Show Image', 'Rotate Image', 'Create Thumbnail', 'Crop Image', 'Flip Image', 'Color Change']
        user_option = st.selectbox('옵션을 선택하세요.', user_option)
        
        if user_option == '선택하세요':
            pass
        
        elif user_option == 'Show Image':
            for img in image_list:
                st.image(img)
                
            st.write('원하는 경로 적어주세요')
            directory = st.text_input('directory: ')
            if st.button('저장하기'):
                for img in image_list:
                    save_uploaded_file(directory, img)


        elif user_option == 'Rotate Image':
            #1. 유저 입력
            user_rotate = st.text_input('회전을 입력하세요!', max_chars=5)
            #print(user_rotate)
            
            transformed_img_list = [] #로테이트 시킨 것을 리스트화해서 저장해주기 위해 리스트 만듬
            #2. 반복문 실행
            if user_rotate != "":
                for img in image_list:
                    rotated_img = img.rotate(int(user_rotate))
                    st.image(rotated_img)
                    transformed_img_list.append(rotated_img) #변형된 (rotated)된 이미지 리스트에 추가
            
            directory = st.text_input('파일 경로 입력하세요')
            if st.button('파일 저장'):
                
                #파일 저장
                for img in transformed_img_list:
                    # 주의 할점은 image_list 는 회전된 이미지가 아니다
                    # rotate된 이미지는 rotated_img 에 들어가 있음 (리스트아님) ---> 리스트로 만들어 줘야지 밑에서 저장할 수 있다
                    
                    save_uploaded_file(directory, img)
                    

        elif user_option == 'Create Thumbnail':
            user_thunbnail_row = st.text_input('원하는 가로 크기를 입력하세요.', max_chars=3)
            user_thunbnail_col = st.text_input('원하는 세로 크기를 입력하세요.', max_chars=3)
            
            if (user_thunbnail_row != "") and (user_thunbnail_col != "") :

                size = (int(user_thunbnail_row), int(user_thunbnail_col))  #size을 튜플로 지정해줌
                
                transformed_thumbnail_list = []
                for img in image_list:
                    #print(img.size)
                    img.thumbnail(size)  #  이미지 자체를 바꿈의 주의 썸네일에서 바로 적용이 되는 듯
                    st.image(img)
                    transformed_thumbnail_list.append(img)

                directory = st.text_input('파일 경로 입력하세요')
                if st.button('파일 저장'):
                    for img in transformed_thumbnail_list:
                        save_uploaded_file(directory, img)        
                    
            else :
                st.warning('가로,세로 다 입력해주세요')

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
                for img in image_list:
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

            #저장하기 위한 리스트 만들기
            
            if status == '수직(위/아래)로 뒤집기':
                transformed_img_list = []
                for img in image_list:
                    flipped_img = img.transpose( Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
            elif status == '수평으로(왼쪽/오른쪽) 뒤집기':
                
                transformed_img_list = []
                for img in image_list:
                    flipped_img = img.transpose( Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            directory = st.text_input('파일 경로 입력하세요')
            if st.button('저장하기'):
                for img in transformed_img_list:
                    save_uploaded_file(directory, img)      



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
                


#         # start_x = st.number_input('시작 x 좌표', 0, img.size[0]-1)
#         # start_y = st.number_input('시작 y 좌표', 0, img.size[0]-1)
#         # max_width = img.size[0] - start_x
#         # max_height = img.size[1] - start_y
#         #width = st.number_input('width 입력', 1, max_width)
#         #height = st.number_input('height 입력', 1, max_height)
#         #box = (start_x, start_y, start_x+width, start_y+height)
#         #나머지는 크랍코드



if __name__ == '__main__':
    main()

